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
        'LandSlide_Risk': request.GET.get('LandSlide_Risk'),
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
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator

def safe_float_conversion(value):
    """Convert to float, return None if conversion fails."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def safe_decimal_conversion(value):
    """Convert to currency formatted string."""
    try:
        return "${:,.2f}".format(float(value)) if value is not None else None
    except (ValueError, TypeError):
        return None

def percentage_conversion(value):
    """Convert to percentage formatted string."""
    try:
        return "{:.2f}%".format(float(value)) if value is not None else None
    except (ValueError, TypeError):
        return None

def number_with_two_decimals(value):
    """Convert to string with two decimal points."""
    try:
        return "{:.2f}".format(float(value)) if value is not None else None
    except (ValueError, TypeError):
        return None

def number_without_decimals(value):
    """Convert to string without decimal points."""
    try:
        return "{:.0f}".format(float(value)) if value is not None else None
    except (ValueError, TypeError):
        return None

from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
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

def calculate_deciles(scores):
    """Calculate deciles based on the list of scores."""
    if not scores:
        return [None] * 10  # Return a list of None if no scores
    min_score = min(scores)
    max_score = max(scores)
    if min_score == max_score:
        return [min_score] * 10
    return [min_score + (max_score - min_score) * i / 10 for i in range(1, 11)]

from collections import OrderedDict
def deep_dive_view(request):
    # Fetch all OmData records where Score is not null
    om_data = OmData.objects.filter(Score__isnull=False)

    # Get search values from request
    search_values = {f"symbol_{i}": request.GET.get(f"symbol_{i}", "").strip() for i in range(1, 9)}

    # Create search conditions
    search_conditions = Q()
    final_symbols = []

    # Populate the search conditions with user input only
    for i in range(1, 9):
        symbol = search_values[f'symbol_{i}']
        if symbol:
            search_conditions |= Q(Symbol__iexact=symbol)
            final_symbols.append(symbol)  # Track actual symbols

    # Filter based on search conditions
    if search_conditions:
        om_data = om_data.filter(search_conditions)

    # Ensure the symbols appear in the same order as the inputs
    ordered_data = []
    for symbol in final_symbols:
        filtered_data = om_data.filter(Symbol__iexact=symbol)
        if filtered_data.exists():
            ordered_data.append(filtered_data.first())

    # Specify fields for display
    display_fields = [
    'Symbol', 'Company', 'Industry_Sector', 'Score', 'Price', 'OM_Target', 'Percentile', 'Price_OM_Target',
    'SS', 'P_SS', 'Percentile28', 'Value', 'Growth', 'Quality', 'Moat', 'Super_Multiple_Predictor', 'Data31',
    'Data11', 'Percentile20', 'Data_6', 'Percentile_6', 'Data_3', 'Percentile_3', 'Data22', 'Percentile26',
    'Data12', 'Percentile27', 'RD_Expenses', 'Percentile14', 'Data14', 'Percentile_22', 'Data16',
    'Percentile_23', 'Data24', 'Percentile24', 'Data23', 'Percentile23', 'Data_1', 'Percentile_1',
    'Data_2', 'Percentile_2', 'Data25', 'Percentile_28', 'Data102', 'Percentile_18', 'Stock_Based_Comp',
    "Percentage_of_Revenue", 'Data8', 'Percentile102', 'SPY3', 'Data9', 'Percentile11', 'SPY4',
    'One_Year_Growth', 'Percentile5', 'Three_Year_Growth', 'Percentile6', 'Five_Year_Growth', 'Percentile7',
    'Data26', 'Percentile18', 'Data30', 'Data_8', 'Percentile_8', 'Data28', 'FCFMarginTrailing',
    'FCFMarginForward', 'Data29', 'Percentile22', 'Data10', 'Percentile10', 'Data_14', 'Percentile17',
    'Data27', 'Percentile2', 'Data_7', 'Percentile_7', 'Data5', 'Percentile_9', 'Data6', 'Percentile_13',
    'Data19', 'Percentile12', 'Data20', 'Percentile13', 'SM_Expenses', 'Data222', 'Data4',
    'Percentile16', 'Data88', 'Percentile183'
]

    # Define labels for each field
    from collections import OrderedDict
    field_labels = OrderedDict([
    ('Symbol', 'Symbol'),
    ('Company', 'Company'),
    ('Industry_Sector', 'Industry'),
    ('Price', 'Price'),  # Convert to currency
    ('Score', 'OM Score'),  # Convert to number with no decimal point
    ('OM_Target', 'OM Price Target'),  # Convert to currency
    ('Percentile', 'OM Score Ranking'),  # Convert to percentage
    ('Price_OM_Target', 'Price/OM Target%'),
    ('SS', 'Sell-Side Target'),  # Convert to currency
    ('P_SS', 'Price/SS Target%'),  # Convert to number with two decimal points
    ('Percentile28', 'Price SS Target % Ranking'),  # Convert to percentage
    ('Value', 'Value'),
    ('Growth', 'Growth'),
    ('Quality', 'Quality'),
    ('Moat', 'Moat'),
    ('Super_Multiple_Predictor', 'Super Multiple Predictor'),
    ('Data31', 'Quality Trio'),  # Convert to number with two decimal points
    ('Data11', 'Short Interest'),  # Convert to number with two decimal points
    ('Percentile20', 'Short Interest Ranking%'),  # Convert to percentage
    ('Data_6', 'Share Repurchases'),  # Convert to number with two decimal points
    ('Percentile_6', 'Share Repurchases Ranking'),  # Convert to percentage
    ('Data_3', 'EV/Sales Trailing'),  # Convert to number with two decimal points
    ('Percentile_3', 'EV/Sales Trailing Ranking'),  # Convert to percentage
    ('Data22', 'EV/Sales Forward'),  # Convert to number with two decimal points
    ('Percentile26', 'EV/Sales Forward Ranking'),  # Convert to percentage
    ('Data12', 'EV/EBITDA Trailing'),  # Convert to number with two decimal points
    ('Percentile27', 'EV/EBITDA Trailing Ranking'),  # Convert to percentage
    ('Data26', 'EBITDA/OCF'),  # Convert to number with two decimal points
    ('Percentile18', 'EBITDA/OCF Rank'),  # Convert to percentage
    ('Data30', 'EV/EBITDA Forward'),  # Convert to number with two decimal points
    ('Percenile_5', 'EV/EBITDA Forward Ranking'),  # Convert to percentage
    ('Data_8', 'EV/EBITDA Margin'),  # Convert to number with two decimal points
    ('Percentile_8', 'EV/EBITDA Margin Ranking'),  # Convert to percentage
    ('Data28', 'Revenue Per Share'),  # Convert to number with two decimal points
    ('FCFMarginTrailing', 'FCF Margin Trailing'),  # Convert to number with two decimal points
    ('FCFMarginForward', 'FCF Margin Forward'),  # Convert to number with two decimal points
    ('Data29', 'EV/FCF'),  # Convert to number with two decimal points
    ('Percentile22', 'EV/FCF Ranking'),  # Convert to percentage
    ('Data10', 'Debt to Equity'),  # Convert to number with two decimal points
    ('Percentile10', 'Debt to Equity Ranking'),  # Convert to percentage
    ('Data_14', 'Altman Z Score'),  # Convert to number with two decimal points
    ('Percentile17', 'Altman Z Score Ranking'),  # Convert to percentage
    ('Data27', 'Interest expense /FCF'),  # Convert to number with two decimal points
    ('Percentile2', 'Interest expense /FCF %'),  # Convert to percentage
    ('Data_7', 'ROE'),  # Convert to number with two decimal points
    ('Percentile_7', 'ROE % Ranking'),  # Convert to percentage
    ('Data5', 'ROIC'),  # Convert to number with two decimal points
    ('Percentile_9', 'ROIC % Ranking'),  # Convert to percentage
    ('Data6', 'Cash Conversion Cycle'),  # Convert to number with two decimal points
    ('Percentile_13', 'Cash Conversion Cycle Ranking'),  # Convert to percentage
    ('Data19', 'DSOs'),  # Convert to number with two decimal points
    ('Percentile12', 'DSO Ranking'),  # Convert to percentage
    ('Data20', 'Inventory Turnover'),  # Convert to number with two decimal points
    ('Percentile13', 'Inventory Turnover Ranking'),  # Convert to percentage
    ('RD_Expenses', 'Research & Development/Sales'),  # Convert to currency
    ('Percentile14', 'R&D Ranking'),  # Convert to percentage
    ('SM_Expenses', 'Sales & Marketing/Sales'),  # Convert to currency
    ('Data222', 'Sales & Marketing/Sales Ranking'),  # Convert to number with two decimal points
    ('Data4', 'Gross Margin'),  # Convert to number with two decimal points
    ('Percentile16', 'Gross Margin Ranking'),  # Convert to percentage
    ('Data15', 'Price/Tangible Book'),  # Convert to number with two decimal points
    ('Percentile_24', 'Price/Tangible Book Ranking'),  # Convert to percentage
    ('Data14', '1 Month Change EBITDA'),  # Convert to number with two decimal points
    ('Percentile_22', '1 Month Change EBITDA Ranking'),  # Convert to percentage
    ('Data16', '1 Month Change in Revenue'),  # Convert to number with two decimal points
    ('Percentile_23', '1 Month Change in Revenue Ranking'),  # Convert to percentage
    ('Data24', '5 year Trailing Sales'),  # Convert to number with two decimal points
    ('Percentile24', '5 year Trailing Sales Rank'),  # Convert to percentage
    ('Data23', '3 year Trailing Sale'),  # Convert to number with two decimal points
    ('Percentile23', '3 year trailing Sales Ranking'),  # Convert to percentage
    ('Data_1', '1 year Trailing Sales'),  # Convert to number with two decimal points
    ('Percentile_1', '1 year Trailing Sales Ranking'),  # Convert to percentage
    ('Data_2', '1 year Farward'),  # Convert to number with two decimal points
    ('Percentile_2', '1 year Farward Ranking'),  # Convert to percentage
    ('Data25', '2 year Forward'),  # Convert to number with two decimal points
    ('Percentile_28', '2 year Forward Ranking'),  # Convert to percentage
    ('Data102', 'Beta'),  # Convert to number with two decimal points
    ('Percentile_18', 'Beta Ranking'),  # Convert to percentage
    ('Stock_Based_Comp', 'Stock Based Comp'),  # Convert to currency
    ('Percentage_of_Revenue', 'Stock Based Comp / Revenue Ranking'),  # Convert to percentage
    ('Data8', '3 month'),  # Convert to number with two decimal points
    ('Percentile102', '3 month ranking'),  # Convert to percentage
    ('SPY3', '3 month SPY'),  # Convert to percentage
    ('Data9', '6 month'),  # Convert to number with two decimal points
    ('Percentile11', '6 month ranking'),  # Convert to percentage
    ('SPY4', '6 month SPY'),  # Convert to percentage
    ('One_Year_Growth', '1 Year Sahre Count Growth'),  # Convert to percentage
    ('Percentile5', '1 Year Share Count Ranking'),  # Convert to percentage
    ('Three_Year_Growth', '3 Year Share Count Growth'),  # Convert to percentage
    ('Percentile6', '3 Year Share Count Ranking'),  # Convert to percentage
    ('Five_Year_Growth', '5 Year Share Count Growth'),  # Convert to percentage
    ('Percentile7', '5 Year Share Count Ranking'),  # Convert to percentage
])

 # Define groups for field formatting
    percentage_fields = [
    'Price_OM_Target', 'One_Year_Growth', 'Three_Year_Growth', 'Five_Year_Growth', 'SPY3', 'SPY4',
    'Percentile', 'Percentile28', 'Percentile20', 'Percentile_6', 'Percentile_3', 'Percentile26',
    'Percentile27', 'Percentile18', 'Percentile_5', 'Percentile_8', 'Percentile22', 'Percentile10',
    'Percentile17', 'Percentile2', 'Percentile_7', 'Percentile_9', 'Percentile_13', 'Percentile12',
    'Percentile13', 'Percentile14', 'Percentile_22', 'Percentile_23', 'Percentile16', 'Percentile_24',
    'Percentile24', 'Percentile23', 'Percentile_1', 'Percentile_2', 'Percentile_28', 'Percentile_18',
    'Percentile102', 'Percentile11', 'Percentile5', 'Percentile6', 'Percentile7', 'Percentage_of_Revenue','Data31'
    ,'Data11', 'Data_8','Data27','Data_7','Data5','Data6','Data20','Data4','P_SS', 'Data16','FCFMarginTrailing', 'Data222'
    ]

    float_fields = [
    'Score', 'Beta','Data_6', 'Data_3', 'Data22', 'Data12', 'Data14','Data15',
    'Data26', 'Data30', 'Data28', 'Data29', 'Data10', 'Data_14', 'Data19', 'Data24',
    'Data23', 'Data_1', 'Data_2', 'Data25', 'Data8', 'Data9'
    ]

    currency_fields = [
    'Price', 'OM_Target', 'SS', 'RD_Expenses', 'Stock_Based_Comp','SM_Expenses'
    ]
    # Convert specific fields to their respective formats
    for item in om_data:
     item.Score = safe_float_conversion(item.Score)
    item.Price = safe_decimal_conversion(item.Price)
    item.OM_Target = safe_decimal_conversion(item.OM_Target)

    Percentile = safe_float_conversion(item.Percentile)
    item.Percentile = (Percentile * 100) if Percentile is not None else None

    item.SS = safe_decimal_conversion(item.SS)
    item.P_SS = safe_float_conversion(item.P_SS)

    Percentile28 = safe_float_conversion(item.Percentile28)
    item.Percentile28 = (Percentile28 * 100) if Percentile28 is not None else None

    item.Data31 = safe_float_conversion(item.Data31)
    item.Data11 = safe_float_conversion(item.Data11)

    Percentile20 = safe_float_conversion(item.Percentile20)
    item.Percentile20 = (Percentile20 * 100) if Percentile20 is not None else None

    item.Data_6 = safe_float_conversion(item.Data_6)

    Percentile_6 = safe_float_conversion(item.Percentile_6)
    item.Percentile_6 = (Percentile_6 * 100) if Percentile_6 is not None else None

    item.Data_3 = safe_float_conversion(item.Data_3)

    Percentile_3 = safe_float_conversion(item.Percentile_3)
    item.Percentile_3 = (Percentile_3 * 100) if Percentile_3 is not None else None

    item.Data22 = safe_float_conversion(item.Data22)

    Percentile26 = safe_float_conversion(item.Percentile26)
    item.Percentile26 = (Percentile26 * 100) if Percentile26 is not None else None

    item.Data12 = safe_float_conversion(item.Data12)

    Percentile27 = safe_float_conversion(item.Percentile27)
    item.Percentile27 = (Percentile27 * 100) if Percentile27 is not None else None

    item.RD_Expenses = safe_decimal_conversion(item.RD_Expenses)

    Percentile14 = safe_float_conversion(item.Percentile14)
    item.Percentile14 = (Percentile14 * 100) if Percentile14 is not None else None

    item.Data14 = safe_float_conversion(item.Data14)

    Percentile_22 = safe_float_conversion(item.Percentile_22)
    item.Percentile_22 = (Percentile_22 * 100) if Percentile_22 is not None else None

    item.Data16 = safe_float_conversion(item.Data16)

    Percentile_23 = safe_float_conversion(item.Percentile_23)
    item.Percentile_23 = (Percentile_23 * 100) if Percentile_23 is not None else None

    item.Data24 = safe_float_conversion(item.Data24)

    Percentile24 = safe_float_conversion(item.Percentile24)
    item.Percentile24 = (Percentile24 * 100) if Percentile24 is not None else None

    item.Data23 = safe_float_conversion(item.Data23)

    Percentile23 = safe_float_conversion(item.Percentile23)
    item.Percentile23 = (Percentile23 * 100) if Percentile23 is not None else None

    item.Data_1 = safe_float_conversion(item.Data_1)

    Percentile_1 = safe_float_conversion(item.Percentile_1)
    item.Percentile_1 = (Percentile_1 * 100) if Percentile_1 is not None else None

    item.Data_2 = safe_float_conversion(item.Data_2)

    Percentile_2 = safe_float_conversion(item.Percentile_2)
    item.Percentile_2 = (Percentile_2 * 100) if Percentile_2 is not None else None

    item.Data25 = safe_float_conversion(item.Data25)

    Percentile_28 = safe_float_conversion(item.Percentile_28)
    item.Percentile_28 = (Percentile_28 * 100) if Percentile_28 is not None else None

    item.Data102 = safe_float_conversion(item.Data102)

    Percentile_18 = safe_float_conversion(item.Percentile_18)
    item.Percentile_18 = (Percentile_18 * 100) if Percentile_18 is not None else None

    item.Stock_Based_Comp = safe_decimal_conversion(item.Stock_Based_Comp)

    Percentage_of_Revenue = safe_float_conversion(item.Percentage_of_Revenue)
    item.Percentage_of_Revenue = (Percentage_of_Revenue * 100) if Percentage_of_Revenue is not None else None

    item.Data8 = safe_float_conversion(item.Data8)

    Percentile102 = safe_float_conversion(item.Percentile102)
    item.Percentile102 = (Percentile102 * 100) if Percentile102 is not None else None

    SPY3 = safe_float_conversion(item.SPY3)
    item.SPY3 = (SPY3 * 100) if SPY3 is not None else None

    item.Data9 = safe_float_conversion(item.Data9)

    Percentile11 = safe_float_conversion(item.Percentile11)
    item.Percentile11 = (Percentile11 * 100) if Percentile11 is not None else None

    SPY4 = safe_float_conversion(item.SPY4)
    item.SPY4 = (SPY4 * 100) if SPY4 is not None else None

    One_Year_Growth = safe_float_conversion(item.One_Year_Growth)
    item.One_Year_Growth = (One_Year_Growth * 100) if One_Year_Growth is not None else None

    Percentile5 = safe_float_conversion(item.Percentile5)
    item.Percentile5 = (Percentile5 * 100) if Percentile5 is not None else None

    Three_Year_Growth = safe_float_conversion(item.Three_Year_Growth)
    item.Three_Year_Growth = (Three_Year_Growth * 100) if Three_Year_Growth is not None else None

    Percentile6 = safe_float_conversion(item.Percentile6)
    item.Percentile6 = (Percentile6 * 100) if Percentile6 is not None else None

    Five_Year_Growth = safe_float_conversion(item.Five_Year_Growth)
    item.Five_Year_Growth = (Five_Year_Growth * 100) if Five_Year_Growth is not None else None

    Percentile7 = safe_float_conversion(item.Percentile7)
    item.Percentile7 = (Percentile7 * 100) if Percentile7 is not None else None

    # Calculate scores for deciles
    scores = [item.Score for item in om_data if item.Score is not None]
    deciles = calculate_deciles(scores)

    # Sort data by Score
    om_data = sorted(om_data, key=lambda x: (x.Score if isinstance(x.Score, (int, float)) else float('-inf')), reverse=True)

    # Pagination
    paginator = Paginator(om_data, 8)  # Adjust per your needs
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    

    # Precompute field values for search inputs
    search_field_values = [search_values.get(f"symbol_{i}", "") for i in range(1, 9)]

    return render(request, 'om/deep_dive_view.html', {
        "page_obj": ordered_data, 
        "page_obj": page_obj,
        'field_names': display_fields,
        'field_labels': field_labels,
        'search_values': search_values,
        'search_field_values': search_field_values,
        'search_field_range': list(range(1, 9)),
        'percentage_fields': percentage_fields,
        'float_fields': float_fields,
        'currency_fields': currency_fields,
        'deciles': deciles,
    })
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
import pandas as pd
from .models import OmData  # Ensure this is the correct model import


# View to manage records
@login_required
def manage_records(request):
    if request.method == 'POST':
        if 'delete_all' in request.POST:
            OmData.objects.all().delete()  # Delete all records
            return redirect('manage_records')  # Redirect to the same page

    data = OmData.objects.all()

    # Extract field names, excluding the 'id' field
    fields = [field.name for field in OmData._meta.fields if field.name != 'id']

    return render(request, 'om/manage_records.html', {'data': data, 'fields': fields})


# View to update a record via AJAX
@csrf_exempt
@login_required
def update_record(request, record_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON body
            record = get_object_or_404(OmData, id=record_id)  # Get the record or return 404

            # Update the record's fields
            for field, value in data.items():
                setattr(record, field, value)
            record.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


# View to delete a specific record
@login_required
def delete_record(request, id):
    try:
        record = OmData.objects.get(id=id)
        record.delete()  # Delete the record
    except OmData.DoesNotExist:
        pass  # Handle the case where the record doesn't exist (optional)

    return redirect('manage_records')  # Redirect back to the manage records page


# View to upload data from an Excel file
@login_required
def upload_om_data(request):
    if request.method == 'POST' and 'excel_file' in request.FILES:
        excel_file = request.FILES['excel_file']
        try:
            df = pd.read_excel(excel_file, dtype=str)
            if 'replace' in request.POST:
                OmData.objects.all().delete()  # Replace existing data

            model_fields = [field.name for field in OmData._meta.fields if field.name != 'id']
            df_filtered = df[model_fields] if all(col in model_fields for col in df.columns) else df[model_fields]

            saved_count = 0
            for _, row in df_filtered.iterrows():
                row_data = {field.name: row[field.name] for field in OmData._meta.fields if field.name != 'id'}
                try:
                    OmData.objects.create(**row_data)
                    saved_count += 1
                except Exception as e:
                    print(f"Error for row: {row_data}. Exception: {e}")

            messages.success(request, f"Successfully saved {saved_count} records.")
            return redirect('home')

        except Exception as e:
            messages.error(request, f"Error uploading file: {e}")

    return render(request, 'om/upload.html')


# View to download data as an Excel file
@login_required
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


# Home view (optional)
def home(request):
    return render(request, 'om/home.html')

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

def om_upside(request):
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
    if request.GET.get('Upside_50_SS_Target') or not request.GET:
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

    upside_50_checked = request.GET.get('Upside_50_SS_Target') or not request.GET  # True if checked or if no GET params

    return render(request, 'om/upside.html', {
        'page_obj': page_obj,
        'field_names': display_fields,
        'field_labels': field_labels,  # Pass the labels dictionary to the template
        'min_score': min_score,
        'max_score': max_score,
        'deciles': deciles,
        'symbol': symbol,
        'display_format': display_format,
        # Checkbox context to keep their state
        'upside_50_checked': upside_50_checked, 
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

# Home view (optional)
def home(request):
    return render(request, 'om/home.html')

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

def om_10upside(request):
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
    if request.GET.get('Greater_90_SS_Target') or not request.GET:  # Apply default filter for Greater_90_SS_Target if no GET parameters
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

    greater_90_checked = request.GET.get('Greater_90_SS_Target') or not request.GET 

    return render(request, 'om/10upside.html', {
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
        'greater_90_checked': greater_90_checked,
        'short_interest': request.GET.get('short_interest'),
        'liquid_loved_late': request.GET.get('liquid_loved_late'),
        'accounting_trouble': request.GET.get('accounting_trouble'),
        'most_expensive': request.GET.get('most_expensive'),
    })

