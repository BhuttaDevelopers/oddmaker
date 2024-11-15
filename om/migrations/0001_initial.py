# Generated by Django 5.0 on 2024-10-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OmData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(max_length=100)),
                ('Company', models.CharField(max_length=100)),
                ('Industry_Sector', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Score', models.IntegerField()),
                ('Percentile', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Score_Without_Short_Scale', models.IntegerField()),
                ('Percentile_00', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Score_Without_Bonus', models.IntegerField()),
                ('Percentile_01', models.DecimalField(decimal_places=2, max_digits=5)),
                ('OM_Target', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Price2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('No_Score_Filter', models.IntegerField()),
                ('OM_Score', models.CharField(max_length=100)),
                ('Value', models.CharField(max_length=100)),
                ('Growth', models.CharField(max_length=100)),
                ('Quality', models.CharField(max_length=100)),
                ('Moat', models.CharField(max_length=100)),
                ('Balance_Sheet', models.CharField(max_length=100)),
                ('Timing', models.CharField(max_length=100)),
                ('Insider_Buying', models.CharField(max_length=100)),
                ('Super_Multiple_Predictor', models.CharField(max_length=100)),
                ('Price_OM_Target', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PCT3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Price_SS_Target', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Value_Raw', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Growth_Raw', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PCT5', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Quality_Raw', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PCT6', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Moat_Raw', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Balance_Sheet_Raw', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SMA_200D', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Timing_Raw', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PCT7', models.DecimalField(decimal_places=2, max_digits=5)),
                ('EV_EBITDA_Trailing', models.FloatField()),
                ('EV_EBITDA_Forward', models.FloatField()),
                ('EV_Sales_Trailing', models.FloatField()),
                ('EV_Sales_Farward2', models.FloatField()),
                ('FCF_EV_Trailing', models.DecimalField(decimal_places=2, max_digits=5)),
                ('FCF_EV_Farward', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Revenue_GrowthFarward', models.FloatField()),
                ('EBITDA_Growth', models.FloatField()),
                ('FCFMarginTrailing', models.FloatField()),
                ('FCFMarginFarward', models.FloatField()),
                ('ROE', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ROIC', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Short_Interest', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Beta', models.FloatField()),
                ('Upside_50_SS_Target', models.CharField(max_length=100)),
                ('Greater_90_SS_Target', models.CharField(max_length=100)),
                ('Great_But_Hated', models.CharField(max_length=100)),
                ('LandSlide_Risk', models.CharField(max_length=100)),
                ('Saftey_Net', models.CharField(max_length=100)),
                ('Glod_Mine', models.CharField(max_length=100)),
                ('Careless_Bucket', models.CharField(max_length=100)),
                ('Liquid_Loved_Late', models.CharField(max_length=100)),
                ('Berkshire_Brain', models.CharField(max_length=100)),
                ('Anti_Berkshire', models.CharField(max_length=100)),
                ('Private_Equity_Model', models.CharField(max_length=100)),
                ('Gems_Ville', models.CharField(max_length=100)),
                ('Bullet_Proof', models.CharField(max_length=100)),
                ('Junk_Yard', models.CharField(max_length=100)),
                ('Accounting_Trouble', models.CharField(max_length=100)),
                ('Hidden_Innovators', models.CharField(max_length=100)),
                ('Multiple_Predictor', models.FloatField()),
                ('Multiplier', models.FloatField()),
                ('EV_Sales', models.IntegerField()),
                ('EV_EBITIDA2', models.IntegerField()),
                ('Super_Multiple_Predictor1', models.IntegerField()),
                ('Percentile29', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Long_Bonus', models.IntegerField()),
                ('Short_Bonus', models.IntegerField()),
                ('Squeeze_Watch', models.IntegerField()),
                ('Market_Cap', models.DecimalField(decimal_places=2, max_digits=10)),
                ('EV', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Revenue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TrailingEBITDA', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TrailingEBITDA_3Y', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TrailingEBITDA_5Y', models.DecimalField(decimal_places=2, max_digits=10)),
                ('FarwardEBITDA', models.DecimalField(decimal_places=2, max_digits=10)),
                ('NetDebt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Trailing_Free_CF', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Farward_Free_CF', models.DecimalField(decimal_places=2, max_digits=10)),
                ('OperCF', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CapEx', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Interest_Expense', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Data_3', models.FloatField()),
                ('Percentile_3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Score_4', models.IntegerField()),
                ('Data22', models.FloatField()),
                ('Percentile26', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data12', models.FloatField()),
                ('Percentile27', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data30', models.FloatField()),
                ('Percentile_5', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Score_5', models.IntegerField()),
                ('SS', models.DecimalField(decimal_places=2, max_digits=10)),
                ('P_SS', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Score_3', models.IntegerField()),
                ('Data29', models.FloatField()),
                ('Percentile22', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data28', models.FloatField()),
                ('Percentile25', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data_8', models.FloatField()),
                ('Percentile_8', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Score_8', models.IntegerField()),
                ('Data_9', models.FloatField()),
                ('Percentile21', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data10', models.FloatField()),
                ('Percentile10', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Current', models.FloatField()),
                ('Shares_Out', models.FloatField()),
                ('One_Year_Growth', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile5', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Shares_Out3', models.FloatField()),
                ('Three_Year_Growth', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile6', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Shares_Out5', models.FloatField()),
                ('Five_Year_Growth', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile7', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data27', models.FloatField()),
                ('Percentile2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data2', models.FloatField()),
                ('Percentile3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data41', models.FloatField()),
                ('Percentile41', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data_1', models.FloatField()),
                ('Percentile_1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Score_1', models.IntegerField()),
                ('Data23', models.FloatField()),
                ('Percentile23', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data24', models.FloatField()),
                ('Percentile24', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data_2', models.FloatField()),
                ('Percentile_2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data25', models.FloatField()),
                ('Percentile_28', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data_18', models.FloatField()),
                ('Percentile4', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data5', models.FloatField()),
                ('Percentile_9', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data31', models.FloatField()),
                ('Data_7', models.FloatField()),
                ('Percentile_7', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Score_7', models.IntegerField()),
                ('Data6', models.FloatField()),
                ('Percentile_13', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data19', models.FloatField()),
                ('Percentile12', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data20', models.FloatField()),
                ('Percentile13', models.DecimalField(decimal_places=2, max_digits=5)),
                ('RD_Expenses', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Data21', models.FloatField()),
                ('Percentile14', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SM_Expenses', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Data222', models.FloatField()),
                ('Percentile15', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data4', models.FloatField()),
                ('Percentile16', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data_14', models.FloatField()),
                ('Percentile17', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data26', models.FloatField()),
                ('Percentile18', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data88', models.FloatField()),
                ('Percentile183', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data13', models.FloatField()),
                ('Percentile19', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data11', models.FloatField()),
                ('Percentile20', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data7', models.FloatField()),
                ('Percentile8', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SPY', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile9', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SPY2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data8', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile102', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SPY3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data9', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile11', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SPY4', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data_6', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Percentile_6', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Score_6', models.IntegerField()),
                ('Data32', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile_12', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data102', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile_18', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Stock_Based_Comp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Percentage_of_Revenue', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile_20', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data14', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile_22', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data16', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile_23', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data15', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile_24', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Data17', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Percentile_25', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ValuePCT', models.DecimalField(decimal_places=2, max_digits=5)),
                ('MoatPCT', models.DecimalField(decimal_places=2, max_digits=5)),
                ('BSPCT', models.DecimalField(decimal_places=2, max_digits=5)),
                ('HolyTrinPCT', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
