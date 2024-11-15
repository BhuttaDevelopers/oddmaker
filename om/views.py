from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import OmData
import pandas as pd
from django.core.exceptions import ValidationError
from decimal import Decimal, InvalidOperation

# Safe conversion functions
def safe_float_conversion(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None  # Return None if conversion fails

def safe_decimal_conversion(value):
    try:
        return Decimal(value)
    except (InvalidOperation, ValueError, TypeError):
        return None  # Return None if conversion fails

def om_data_list(request):
    # Fetch all OmData records where Score is not null
    om_data = OmData.objects.filter(Score__isnull=False)

    # Apply filters based on checkboxes and search criteria
    filters = Q()
    
    # Filter by symbol if provided
    symbol = request.GET.get('symbol', '')  # Default to empty string if symbol not provided
    if symbol:
       filters &= Q(Symbol__iexact=symbol)
    
    # Apply filters for checkbox fields
    # Long Idea Searches Checkboxes
    if request.GET.get('Upside_50_SS_Target'):
        filters &= Q(Upside_50_SS_Target="Yes")

    if request.GET.get('great_but_hated'):
        filters &= Q(Great_But_Hated="Yes")

    if request.GET.get('gold_mine'):
        filters &= Q(Glod_Mine="Yes")

    if request.GET.get('berkshire_brain'):
        filters &= Q(Berkshire_Brain="Yes")

    if request.GET.get('safety_net'):
        filters &= Q(Saftey_Net="Yes")

    if request.GET.get('private_equity_model'):
        filters &= Q(Private_Equity_Model="Yes")

    if request.GET.get('bullet_proof'):
        filters &= Q(Bullet_Proof="Yes")

    if request.GET.get('hidden_innovators'):
        filters &= Q(Hidden_Innovators="Yes")

    if request.GET.get('Gems_Ville'):
        filters &= Q(Gems_Ville="Yes")

    if request.GET.get('One_Year_Growth'):
        filters &= Q( One_Year_Growth__gte=-35) & Q( One_Year_Growth__lte=-1)
# Short Idea Searches Checkboxes
    if request.GET.get('Greater_90_SS_Target'):
        filters &= Q(Greater_90_SS_Target="Yes")

    if request.GET.get('short_interest'):  # Ensure this matches the checkbox name
    # Check the Short Interest condition in its original float form (not percentage)
         filters &= Q(Short_Interest__gte=0.05) & Q(Short_Interest__lte=0.90)

    if request.GET.get('liquid_loved_late'):
        filters &= Q(Liquid_Loved_Late="Yes")

    if request.GET.get('landslide_risk'):
        filters &= Q(LandSlide_Risk="Yes")

    if request.GET.get('junk_yard'):
        filters &= Q(Junk_Yard="Yes")

    if request.GET.get('accounting_trouble'):
        filters &= Q(Accounting_Trouble="Yes")

    if request.GET.get('most_expensive'):
        filters &= Q(Most_Expensive="Yes")
    # Repeat for other checkboxes as needed...

    # Apply the filters to the queryset
    om_data = om_data.filter(filters)

    # Convert specific fields to numbers for sorting or display purposes
    for item in om_data:
        item.Score = safe_float_conversion(item.Score)
        Multiple_Predictor = safe_float_conversion(item.Multiple_Predictor)
        item.EV_EBITDA_Trailing = safe_float_conversion(item.EV_EBITDA_Trailing)
        item.EV_EBITDA_Forward = safe_float_conversion(item.EV_EBITDA_Forward)
        item.EV_Sales_Trailing = safe_float_conversion(item.EV_Sales_Trailing)
        item.EV_Sales_Farward2 = safe_float_conversion(item.EV_Sales_Farward2)
        item.Upside_50_SS_Target = safe_float_conversion(item.Upside_50_SS_Target)
        one_year_growth = safe_float_conversion(item.One_Year_Growth)
        item.One_Year_Growth = (one_year_growth * 100) if one_year_growth is not None else None
        Short_Interest = safe_float_conversion(item.Short_Interest)
        item.Short_Interest = (Short_Interest * 100) if Short_Interest is not None else None
        FCF_EV_Trailing = safe_float_conversion(item.FCF_EV_Trailing)
        item.FCF_EV_Trailing = (FCF_EV_Trailing * 100) if FCF_EV_Trailing is not None else None
        FCF_EV_Farward = safe_float_conversion(item.FCF_EV_Farward)
        item.FCF_EV_Farward = (FCF_EV_Farward * 100) if FCF_EV_Farward is not None else None
        Revenue_GrowthFarward= safe_float_conversion(item.Revenue_GrowthFarward)
        FCFMarginTrailing = safe_float_conversion(item.FCFMarginTrailing)
        item.FCFMarginTrailing = (FCFMarginTrailing * 100) if FCFMarginTrailing is not None else None
        FCFMarginFarward = safe_float_conversion(item.FCFMarginFarward)
        item.FCFMarginFarward = (FCFMarginFarward * 100) if FCFMarginFarward is not None else None
        item.Price = safe_decimal_conversion(item.Price)
        item.SS = safe_decimal_conversion(item.SS)# Convert Price to decimal for currency
        item.OM_Target = safe_decimal_conversion(item.OM_Target)  # Convert OM_Target to decimal
        FCFMarginTrailing = safe_float_conversion(item.FCFMarginTrailing)
        item.FCFMarginTrailing = (FCFMarginTrailing * 100) if FCFMarginTrailing is not None else None
        FCFMarginFarward = safe_float_conversion(item.FCFMarginFarward)
        item.FCFMarginFarward = (FCFMarginFarward * 100) if FCFMarginFarward is not None else None
        ROE = safe_float_conversion(item.ROE)
        item.ROE = (ROE * 100) if ROE is not None else None
        ROIC = safe_float_conversion(item.ROIC)
        item.ROIC = (ROIC * 100) if ROIC is not None else None
        Beta = safe_float_conversion(item.Beta)
        if item.Liquid_Loved_Late == "Yes":item.Liquid_Loved_Late = "Yes"
        else: item.Liquid_Loved_Late = "" 
        if item.Great_But_Hated == "Yes": item.Great_But_Hated = "Yes"
        else: item.Great_But_Hated = "" 
        if item.LandSlide_Risk == "Yes": item.LandSlide_Risk = "Yes"
        else: item.LandSlide_Risk = ""  # Set to empty if it's not "Yes"
        if item.Most_Expensive == "Yes": item.Most_Expensive = "Yes"
        else: item.Most_Expensive = ""  # Set to empty if it's not "Yes"
        if item.Saftey_Net == "Yes": item.Saftey_Net = "Yes"
        else: item.Saftey_Net = ""  # Set to empty if it's not "Yes"
        item.Glod_Mine = "Yes" if item.Glod_Mine == "Yes" else ""
        item.Careless_Bucket = "Yes" if item.Careless_Bucket == "Yes" else ""
        item.Berkshire_Brain = "Yes" if item.Berkshire_Brain == "Yes" else ""
        item.Anti_Berkshire = "Yes" if item.Anti_Berkshire == "Yes" else ""
        item.Private_Equity_Model = "Yes" if item.Private_Equity_Model == "Yes" else ""
        item.Gems_Ville = "Yes" if item.Gems_Ville == "Yes" else ""
        item.Bullet_Proof = "Yes" if item.Bullet_Proof == "Yes" else ""
        item.Junk_Yard = "Yes" if item.Junk_Yard == "Yes" else ""
        item.Accounting_Trouble = "Yes" if item.Accounting_Trouble == "Yes" else ""
        item.Hidden_Innovators = "Yes" if item.Hidden_Innovators == "Yes" else ""
        item.Upside_50_SS_Target = "Yes" if item.Upside_50_SS_Target == "Yes" else ""
        item.Greater_90_SS_Target = "Yes" if item.Greater_90_SS_Target == "Yes" else ""


    # Sort data by Score
    om_data = sorted(om_data, key=lambda x: (x.Score if x.Score is not None else float('-inf')), reverse=True)

    # Decile calculation for Score
    scores = [item.Score for item in om_data if item.Score is not None]
    min_score = min(scores) if scores else 0
    max_score = max(scores) if scores else 0

    def calculate_deciles(min_score, max_score):
        if min_score == max_score:
            return [min_score] * 10
        return [min_score + (max_score - min_score) * i // 10 for i in range(1, 11)]

    deciles = calculate_deciles(min_score, max_score)

    # Define labels with line breaks for each field
    field_labels = {
        'Symbol': 'Symbol',
        'Company': 'Company',
        'Industry_Sector': 'Industry<br>Sector',
        'Score': 'OM Score',
        'Price': 'Price',
        'Price_OM_Target1':'Price<br>OMTarget',
        'OM_Target':'Oddsmaker<br>PriceTarget',
        'One_Year_Growth':'Share<br>Repurchases',
        'Short_Interest':'Short<br>Interest',
        'Price_SS_Target1':'Price/SS<br>Target', 
        'Value':'Value',
        'Quality':'Quality', 
        'Growth':'Growth', 
        'Moat':'Moat', 
        'Balance_Sheet':'Balance<br>Sheet', 
        'Timing':'Timing', 
        'Insider_Buying':'Insider<br>Buying',
        'Multiple_Predictor':'Multiple<br>Predictor', 
        'SS':'Sell-Side<br>Target', 
        'EV_EBITDA_Trailing':'EV_EBITDA<br>Trailing', 
        'EV_EBITDA_Forward':'EV_EBITDA<br>Forward', 
        'EV_Sales_Trailing':'EV_Sales<br>Trailing', 
        'EV_Sales_Farward2':'EV_Sales<br>Farward', 
        'FCF_EV_Trailing':'FCF_EV<br>Trailing', 
        'FCF_EV_Farward':'FCF_EV<br>Farward', 
        'Revenue_GrowthFarward':'Revenue<br>GrowthFarward', 
        'FCFMarginTrailing':'FCFMargin<br>Trailing', 
        'FCFMarginFarward':'FCFMargin<br>Farward', 
        'ROE':'ROE', 
        'ROIC':'ROIC', 
        'Beta':'Beta',
        'Liquid_Loved_Late':'Liquid<br>Loved_Late', 
        'Great_But_Hated':'Great<br>But_Hated',
        'LandSlide_Risk':'LandSlide<br>Risk', 
        'Most_Expensive':'Most<br>Expensive',
        'Saftey_Net':'Safety<br>Net', 
        'Glod_Mine':'Glod<br>Mine', 
        'Careless_Bucket':'Careless<br>Bucket', 
        'Berkshire_Brain':'Berkshire<br>Brain', 
        'Anti_Berkshire':'Anti<br>Berkshire', 
        'Private_Equity_Model':'Private<br>Equity_Model', 
        'Gems_Ville':'Gems Ville', 
        'Bullet_Proof':'Bullet Proof', 
        'Junk_Yard':'Junk Yard', 
        'Accounting_Trouble':'Accounting<br>Trouble', 
        'Hidden_Innovators':'Hidden<br>Innovators', 
        'Upside_50_SS_Target':'50%+ Upsideto<br>SS Target', 
        'Greater_90_SS_Target':'>90%SS<br>Target'
        
        # Add labels for other fields similarly
    }

    # Determine display fields based on selected display format
    display_format = request.GET.get('display_format', 'letter_grades')  # Default to letter_grades
    if display_format == 'oddsmaker_score':
        display_fields = ['Symbol', 'Company', 'Industry_Sector', 'Score', 'Price', 'OM_Target', 'One_Year_Growth', 'Short_Interest', 'Price_OM_Target1', 'Multiple_Predictor', 'SS', 'EV_EBITDA_Trailing', 'EV_EBITDA_Forward', 'EV_Sales_Trailing', 'EV_Sales_Farward2', 'FCF_EV_Trailing', 'FCF_EV_Farward', 'Revenue_GrowthFarward', 'FCFMarginTrailing', 'FCFMarginFarward', 'ROE', 'ROIC', 'Beta']
    elif display_format == 'letter_grades':
        display_fields = ['Symbol', 'Company', 'Industry_Sector', 'Score', 'Price', 'Price_OM_Target1', 'One_Year_Growth', 'Short_Interest', 'Price_SS_Target1', 'Value', 'Quality', 'Growth', 'Moat', 'Balance_Sheet', 'Timing', 'Insider_Buying']
    elif display_format == 'risk_profiles':
        display_fields = ['Symbol', 'Company', 'Industry_Sector', 'Liquid_Loved_Late', 'Great_But_Hated', 'LandSlide_Risk', 'Most_Expensive', 'Saftey_Net', 'Glod_Mine', 'Careless_Bucket', 'Berkshire_Brain', 'Anti_Berkshire', 'Private_Equity_Model', 'Gems_Ville', 'Bullet_Proof', 'Junk_Yard', 'Accounting_Trouble', 'Hidden_Innovators', 'Upside_50_SS_Target', 'Greater_90_SS_Target']
    elif display_format == 'multiple_predictor':
        display_fields = ['Symbol', 'Company', 'Industry_Sector', 'Score', 'Price', 'OM_Target', 'Short_Interest', 'Multiple_Predictor']

    # Pagination
    paginator = Paginator(om_data, 3000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'om/data_list.html', {
        'page_obj': page_obj,
        'field_names': display_fields,
        'field_labels': field_labels,  # Pass the labels dictionary to the template
        'min_score': min_score,
        'max_score': max_score,
        'deciles': deciles,
        'symbol': symbol,
        'display_format': display_format,
        # Checkbox context to keep their state
        'upside_50': request.GET.get('upside_50'),
        'great_but_hated': request.GET.get('great_but_hated'),
        'gold_mine': request.GET.get('gold_mine'),
        'berkshire_brain': request.GET.get('berkshire_brain'),
        'safety_net': request.GET.get('safety_net'),
        'private_equity_model': request.GET.get('private_equity_model'),
        'bullet_proof': request.GET.get('bullet_proof'),
        'hidden_innovators': request.GET.get('hidden_innovators'),
        'long_option_ideas': request.GET.get('long_option_ideas'),
        'share_repurchases': request.GET.get('share_repurchases'),
        'greater_90': request.GET.get('greater_90'),
        'short_interest': request.GET.get('short_interest'),
        'liquid_loved_late': request.GET.get('liquid_loved_late'),
        'accounting_trouble': request.GET.get('accounting_trouble'),
        'most_expensive': request.GET.get('most_expensive'),
    })



def upload_om_data(request):
    if request.method == 'POST' and 'excel_file' in request.FILES:
        excel_file = request.FILES['excel_file']
        try:
            df = pd.read_excel(excel_file, dtype=str)  # Load all columns as strings
            print("Columns in the uploaded Excel file:", df.columns.tolist())

            if 'replace' in request.POST:
                OmData.objects.all().delete()

            model_fields = [field.name for field in OmData._meta.fields if field.name != 'id']
            df_filtered = df[model_fields] if all(col in model_fields for col in df.columns) else df[model_fields]

            # Logging the filtered DataFrame
            print("Filtered DataFrame:\n", df_filtered)

            # Save each row to the database
            saved_count = 0
            for _, row in df_filtered.iterrows():
                row_data = {}
                for field in OmData._meta.fields:
                    if field.name != 'id':
                        value = row[field.name]
                        row_data[field.name] = value  # Store all values as text

                print(f"Row data being processed: {row_data}")  # Log row data

                # Attempt to create the object and catch validation errors
                try:
                    OmData.objects.create(**row_data)
                    saved_count += 1
                except ValidationError as e:
                    print(f"Validation error for row: {row_data}. Error: {e}")

            print(f"Successfully saved {saved_count} records.")
            messages.success(request, "Data uploaded successfully!")
            return redirect('data_list')

        except Exception as e:
            messages.error(request, f"Error uploading file: {e}")
            print(f"Error: {e}")

    return render(request, 'om/upload.html')

def home(request):
    return render(request, 'om/home.html')

def download_excel(request):
    data = OmData.objects.all().values()
    if data.exists():
        df = pd.DataFrame(data)
    else:
        field_names = [field.name for field in OmData._meta.fields]
        df = pd.DataFrame(columns=field_names)

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="om_data.xlsx"'
    df.to_excel(response, index=False)
    return response
from django.shortcuts import render
from .models import OmData

def om_data_letter_grades_view(request):
    # Fetch all OmData records where Score is not null
    om_data = OmData.objects.filter(Score__isnull=False)

    # Specify fields for the letter grades display format
    display_fields = [
        'Symbol', 'Company', 'Industry_Sector', 'Score', 'Price', 
        'Price_OM_Target1', 'One_Year_Growth', 'Short_Interest', 
        'Price_SS_Target1', 'Value', 'Quality', 'Growth', 
        'Moat', 'Balance_Sheet', 'Timing', 'Insider_Buying'
    ]

    # Define labels for each field
    field_labels = {
        'Symbol': 'Symbol',
        'Company': 'Company',
        'Industry_Sector': 'Industry<br>Sector',
        'Score': 'OM Score',
        'Price': 'Price',
        'Price_OM_Target1': 'Price<br>OMTarget',
        'One_Year_Growth': 'Share<br>Repurchases',
        'Short_Interest': 'Short<br>Interest',
        'Price_SS_Target1': 'Price/SS<br>Target', 
        'Value': 'Value',
        'Quality': 'Quality', 
        'Growth': 'Growth', 
        'Moat': 'Moat', 
        'Balance_Sheet': 'Balance<br>Sheet', 
        'Timing': 'Timing', 
        'Insider_Buying': 'Insider<br>Buying',
    }

    # Convert specific fields to numbers for sorting or display purposes
    for item in om_data:
        item.Score = safe_float_conversion(item.Score)
        item.Price = safe_decimal_conversion(item.Price)
        item.Short_Interest = safe_float_conversion(item.Short_Interest)

    # Sort data by Score
    om_data = sorted(om_data, key=lambda x: (x.Score if x.Score is not None else float('-inf')), reverse=True)

    # Pagination
    paginator = Paginator(om_data, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'om/letter_grades_view.html', {
        'page_obj': page_obj,
        'field_names': display_fields,
        'field_labels': field_labels,
        'min_score': None,
        'max_score': None,
        'deciles': [],
    })

def download_pdf(request):
    # Create a response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data_list.pdf"'

    # Create a PDF object in landscape mode
    p = canvas.Canvas(response, pagesize=landscape(letter))
    width, height = landscape(letter)

    # Fetch all OmData records
    om_data = OmData.objects.all()

    # Define the table headers
    headers = [
        'Symbol', 'Company', 'Industry/Sector', 'OM Score', 'Current Price', 
        'Price OM Target 1', '1-Year Growth (%)', 'Short Interest (%)', 
        'Price SS Target 1', 'Value Score', 'Quality Score', 
        'Growth Score', 'Moat Rating', 'Balance Sheet Rating', 
        'Timing Score', 'Insider Buying Activity'
    ]

    # Set initial positions
    x = 50
    y = height - 50

    # Print headers
    for header in headers:
        p.drawString(x, y, header)
        x += 100  # Adjust spacing as needed

    # Reset x and move down for the first data row
    x = 50
    y -= 20

    # Iterate through the data and print it
    for item in om_data:
        if y < 50:  # If we're too close to the bottom, create a new page
            p.showPage()
            p.setFont("Helvetica", 10)
            y = height - 50
            # Reprint headers on the new page
            x = 50
            for header in headers:
                p.drawString(x, y, header)
                x += 100
            y -= 20  # Move down for data rows

        # Print each field in the record
        p.drawString(x, y, str(item.Symbol))
        p.drawString(x + 100, y, str(item.Company))
        p.drawString(x + 200, y, str(item.Industry_Sector))
        p.drawString(x + 300, y, str(item.Score))
        p.drawString(x + 400, y, str(item.Price))
        p.drawString(x + 500, y, str(item.Price_OM_Target1))
        p.drawString(x + 600, y, str(item.One_Year_Growth))
        p.drawString(x + 700, y, str(item.Short_Interest))
        p.drawString(x + 800, y, str(item.Price_SS_Target1))
        p.drawString(x + 900, y, str(item.Value))
        p.drawString(x + 1000, y, str(item.Quality))
        p.drawString(x + 1100, y, str(item.Growth))
        p.drawString(x + 1200, y, str(item.Moat))
        p.drawString(x + 1300, y, str(item.Balance_Sheet))
        p.drawString(x + 1400, y, str(item.Timing))
        p.drawString(x + 1500, y, str(item.Insider_Buying))
        
        y -= 20  # Move down for the next row

    # Finalize and save the PDF
    p.showPage()
    p.save()

    return response

def om_data_TheOddsMaker_view(request):
    # Fetch all OmData records
    om_data = OmData.objects.all()

    # Specify the fields to retrieve
    display_fields = [
       'Symbol', 'Company', 'Industry_Sector', 'Score', 'Price', 
       'OM_Target', 'One_Year_Growth', 'Short_Interest', 'Price_OM_Target1', 
       'Multiple_Predictor', 'SS', 'EV_EBITDA_Trailing', 'EV_EBITDA_Forward',
       'EV_Sales_Trailing', 'EV_Sales_Farward2', 'FCF_EV_Trailing', 'FCF_EV_Farward', 
       'Revenue_GrowthFarward', 'FCFMarginTrailing', 'FCFMarginFarward', 'ROE', 'ROIC', 'Beta']
       # Define custom labels for each field
    field_labels = {
          
        'Symbol': 'Symbol',
        'Company': 'Company',
        'Industry_Sector': 'Industry<br>Sector',
        'Score': 'OM Score',
        'Price': 'Price',
        'Price_OM_Target1':'Price<br>OMTarget',
        'OM_Target':'Oddsmaker<br>PriceTarget',
        'One_Year_Growth':'Share<br>Repurchases',
        'Short_Interest':'Short<br>Interest',
        'Multiple_Predictor':'Multiple<br>Predictor', 
        'SS':'Sell-Side<br>Target', 
        'EV_EBITDA_Trailing':'EV_EBITDA<br>Trailing', 
        'EV_EBITDA_Forward':'EV_EBITDA<br>Forward', 
        'EV_Sales_Trailing':'EV_Sales<br>Trailing', 
        'EV_Sales_Farward2':'EV_Sales<br>Farward', 
        'FCF_EV_Trailing':'FCF_EV<br>Trailing', 
        'FCF_EV_Farward':'FCF_EV<br>Farward', 
        'Revenue_GrowthFarward':'Revenue<br>GrowthFarward', 
        'FCFMarginTrailing':'FCFMargin<br>Trailing', 
        'FCFMarginFarward':'FCFMargin<br>Farward', 
        'ROE':'ROE', 
        'ROIC':'ROIC', 
        'Beta':'Beta',
               
        # Add labels for other fields similarly
    
    }

    # Convert specific fields to numbers for sorting or display purposes
    for item in om_data:
        item.Score = safe_float_conversion(item.Score)
        item.Price = safe_decimal_conversion(item.Price)
        item.Short_Interest = safe_float_conversion(item.Short_Interest)

    # Sort data by Score
    om_data = sorted(om_data, key=lambda x: (x.Score if x.Score is not None else float('-inf')), reverse=True)

    # Pagination
    paginator = Paginator(om_data, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'om/TheOddsmaker_view.html', {
        'page_obj': page_obj,
        'field_names': display_fields,
        'field_labels': field_labels,  # Pass the labels dictionary to the template
        'min_score': None,
        'max_score': None,
        'deciles': [],
    })


