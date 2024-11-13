from django.db import models

class OmData(models.Model):
    Symbol = models.CharField(max_length=100, null=True, blank=True) # text field
    Company = models.CharField(max_length=100, null=True, blank=True) # text field
    Industry_Sector= models.CharField(max_length=100, null=True, blank=True) # text field
    Price = models.CharField(max_length=100, null=True, blank=True) # currency field
    Score = models.CharField(max_length=100,  null=True, blank=True) # nuumber with no decimale point
    Percentile = models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Score_Without_Short_Scale= models.CharField(max_length=100,null=True, blank=True)# nuumber with no decimale point
    Percentile_00 = models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Score_Without_Bonus=models.CharField(max_length=100,null=True, blank=True) # number without decimal point
    Percentile_01= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    OM_Target= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Price2 = models.CharField(max_length=100,  null=True, blank=True) # currency field
    No_Score_Filter = models.CharField(max_length=100,null=True, blank=True) # number without decimal point
    OM_Score= models.CharField(max_length=100, null=True, blank=True) # text field
    Price_SS_Target1= models.CharField(max_length=100,null=True, blank=True) # text field not comming in result
    Price_OM_Target1= models.CharField(max_length=100,null=True, blank=True) # text field field not comming in result
    Value= models.CharField(max_length=100, null=True, blank=True) # text field
    Growth= models.CharField(max_length=100, null=True, blank=True) # text field
    Quality= models.CharField(max_length=100, null=True, blank=True) # text field
    Moat= models.CharField(max_length=100, null=True, blank=True) # text field
    Balance_Sheet= models.CharField(max_length=100, null=True, blank=True) # text field
    Timing= models.CharField(max_length=100, null=True, blank=True) # text field
    Insider_Buying= models.CharField(max_length=100, null=True, blank=True) # text field
    Super_Multiple_Predictor= models.CharField(max_length=100, null=True, blank=True) # text field
    Price_OM_Target= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    PCT3= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Price_SS_Target= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Value_Raw= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Growth_Raw= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    PCT5=models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Quality_Raw= models.CharField(max_length=100, null=True, blank=True) # percentage field
    PCT6= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Moat_Raw=models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Balance_Sheet_Raw=models.CharField(max_length=100,  null=True, blank=True) # percentage field
    SMA_200D= models.CharField(max_length=100,  null=True, blank=True) # currency field
    Timing_Raw=models.CharField(max_length=100,  null=True, blank=True) # percentage field
    PCT7= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    EV_EBITDA_Trailing= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    EV_EBITDA_Forward= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    EV_Sales_Trailing= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    EV_Sales_Farward2= models.CharField(max_length=100,null=True, blank=True) # number with 2 decial points
    FCF_EV_Trailing= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    FCF_EV_Farward= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Revenue_GrowthFarward= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    EBITDA_Growth= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    FCFMarginTrailing= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    FCFMarginFarward= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    ROE= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    ROIC= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Short_Interest= models.CharField(max_length=100, null=True, blank=True) # percentage field
    Beta= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Upside_50_SS_Target=  models.CharField(max_length=100, null=True, blank=True) # text field
    Greater_90_SS_Target= models.CharField(max_length=100, null=True, blank=True) # text field
    Liquid_Loved_Late = models.CharField(max_length=100, null=True, blank=True) # text field comming in wrong order
    Great_But_Hated = models.CharField(max_length=100, null=True, blank=True) # text field
    LandSlide_Risk = models.CharField(max_length=100, null=True, blank=True) # text field
    Most_Expensive = models.CharField(max_length=100, null=True, blank=True) # text field
    Saftey_Net = models.CharField(max_length=100, null=True, blank=True) # text field
    Glod_Mine = models.CharField(max_length=100, null=True, blank=True) # text field
    Careless_Bucket = models.CharField(max_length=100, null=True, blank=True) # text field    
    Berkshire_Brain = models.CharField(max_length=100, null=True, blank=True) # text field
    Anti_Berkshire = models.CharField(max_length=100, null=True, blank=True) # text field
    Private_Equity_Model = models.CharField(max_length=100,null=True, blank=True) # text field
    Gems_Ville= models.CharField(max_length=100, null=True, blank=True) # text field
    Bullet_Proof= models.CharField(max_length=100, null=True, blank=True) # text field
    Junk_Yard= models.CharField(max_length=100, null=True, blank=True) # text field
    Accounting_Trouble= models.CharField(max_length=100, null=True, blank=True) # text field
    Hidden_Innovators= models.CharField(max_length=100, null=True, blank=True) # text field
    Multiple_Predictor= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Multiplier= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    EV_Sales = models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    EV_EBITIDA2 = models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    Super_Multiple_Predictor1=models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    Percentile29= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Long_Bonus=models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    Short_Bonus=models.CharField(max_length=100,null=True, blank=True) # number without decimal point
    Squeeze_Watch=models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    Market_Cap = models.CharField(max_length=100,  null=True, blank=True) # currency field
    EV = models.CharField(max_length=100,  null=True, blank=True) # currency field
    Revenue = models.CharField(max_length=100,  null=True, blank=True) # currency field
    TrailingEBITDA = models.CharField(max_length=100,  null=True, blank=True) # currency field
    TrailingEBITDA_3Y = models.CharField(max_length=100,  null=True, blank=True) # currency field
    TrailingEBITDA_5Y = models.CharField(max_length=100,  null=True, blank=True) # currency field
    FarwardEBITDA = models.CharField(max_length=100,  null=True, blank=True) # currency field
    NetDebt = models.CharField(max_length=100,  null=True, blank=True) # currency field
    Trailing_Free_CF= models.CharField(max_length=100,  null=True, blank=True) # currency field
    Farward_Free_CF= models.CharField(max_length=100, null=True, blank=True) # currency field
    OperCF= models.CharField(max_length=100,  null=True, blank=True) # currency field
    CapEx= models.CharField(max_length=100,  null=True, blank=True) # currency field
    Interest_Expense=models.CharField(max_length=100,  null=True, blank=True) # currency field
    Data_3= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile_3= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Score_4=models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    Data22= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile26= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data12= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile27= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data30= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile_5= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Score_5=models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    SS= models.CharField(max_length=100,  null=True, blank=True) # currency field
    P_SS= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile28= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Score_3=models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    Data29= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile22= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data28= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile25= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data_8= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile_8= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Score_8=models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    Data_9= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile21= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data10= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile10= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Current= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Shares_Out= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    One_Year_Growth= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile5= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Shares_Out3= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Three_Year_Growth= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile6= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Shares_Out5= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Five_Year_Growth= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile7= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data27= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile2= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data2= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile3= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data41= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile41= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data_1= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile_1= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Score_1=models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    Data23= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile23= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data24= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile24= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data_2= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile_2= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data25= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile_28= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data_18= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile4= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data5= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile_9= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data31= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Data_7= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile_7= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Score_7=models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    Data6= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile_13= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data19= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile12= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data20= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile13= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    RD_Expenses= models.CharField(max_length=100,  null=True, blank=True) # currency field
    Data21= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile14= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    SM_Expenses= models.CharField(max_length=100,  null=True, blank=True) # currency field
    Data222= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile15= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data4= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile16= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data_14= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile17= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data26= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile18= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data88= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile183= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data13= models.CharField(max_length=100,null=True, blank=True) # number with 2 decial points
    Percentile19= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data11= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile20= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data7= models.CharField(max_length=100,  null=True, blank=True) # number with 2 decial points
    Percentile8= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    SPY= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile9= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    SPY2= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data8= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile102= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    SPY3= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data9= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile11= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    SPY4= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data_6= models.CharField(max_length=100,  null=True, blank=True) # currency field
    Percentile_6= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Score_6=models.CharField(max_length=100,  null=True, blank=True) # number without decimal point
    Data32= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile_12= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data102= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile_18= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Stock_Based_Comp= models.CharField(max_length=100, null=True, blank=True) # currency field
    Percentage_of_Revenue = models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile_20= models.CharField(max_length=100,  null=True, blank=True) # percentage 
    Data14= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile_22= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data16= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile_23= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data15= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile_24= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Data17= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    Percentile_25= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    ValuePCT= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    MoatPCT= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    BSPCT= models.CharField(max_length=100,  null=True, blank=True) # percentage field
    HolyTrinPCT= models.CharField(max_length=100,  null=True, blank=True) # percentage field
def __str__(self):
        return self.Symbol
