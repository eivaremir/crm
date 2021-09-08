# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    account_number = models.CharField(primary_key=True, max_length=40)
    account_name = models.CharField(max_length=45, blank=True, null=True)
    assigned_to = models.CharField(max_length=45, blank=True, null=True)
    assigned_to_code = models.CharField(max_length=45, blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(db_column='IP', max_length=35, blank=True, null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(blank=True, null=True)
    account_status = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=2, blank=True, null=True)
    recovery_question = models.CharField(db_column='Recovery_Question', max_length=45, blank=True, null=True)  # Field name made lowercase.
    recovery_answer = models.CharField(max_length=45, blank=True, null=True)
    compliance_completed = models.IntegerField(blank=True, null=True)
    trading_disabled = models.IntegerField(blank=True, null=True)
    last_comment_time = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    password_reset_token = models.CharField(max_length=100, blank=True, null=True)
    token_timestamp = models.CharField(max_length=45, blank=True, null=True)
    client_type = models.IntegerField(blank=True, null=True)
    primary_phone = models.CharField(max_length=25, blank=True, null=True)
    primary_email = models.CharField(max_length=45, blank=True, null=True)
    mobile_phone = models.CharField(max_length=45, blank=True, null=True)
    prefix = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    address2 = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    documents_verified = models.IntegerField(blank=True, null=True)
    lead_source = models.CharField(max_length=20, blank=True, null=True)
    utm_source = models.CharField(db_column='UTM_Source', max_length=45, blank=True, null=True)  # Field name made lowercase.
    utm_campaign = models.CharField(db_column='UTM_Campaign', max_length=45, blank=True, null=True)  # Field name made lowercase.
    utm_medium = models.CharField(db_column='UTM_Medium', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ftd_amount = models.DecimalField(db_column='FTD_Amount', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ftd_status = models.IntegerField(db_column='FTD_Status', blank=True, null=True)  # Field name made lowercase.
    ftd_date = models.DateTimeField(db_column='FTD_Date', blank=True, null=True)  # Field name made lowercase.
    ftd_currency = models.CharField(db_column='FTD_Currency', max_length=4, blank=True, null=True)  # Field name made lowercase.
    redeposit_status = models.IntegerField(db_column='Redeposit_Status', blank=True, null=True)  # Field name made lowercase.
    total_deposited_usd = models.DecimalField(db_column='Total_deposited_USD', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_deposited_eur = models.DecimalField(db_column='Total_deposited_EUR', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_withdrawn_usd = models.DecimalField(db_column='Total_Withdrawn_USD', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_withdrawn_eur = models.DecimalField(db_column='Total_Withdrawn_EUR', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ftd_owner = models.CharField(db_column='FTD_Owner', max_length=45, blank=True, null=True)  # Field name made lowercase.
    primary_tp_account = models.CharField(db_column='Primary_TP_ACCOUNT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email_subscribed = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)

    
    class Meta:
        managed = False
        db_table = 'ACCOUNTS'


    def __str__(self):
        return f"{self.account_number} - {self.account_name }"
        


class FinancialStatements(models.Model):
    tpa = models.IntegerField(db_column='TPA', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=65, decimal_places=2)  # Field name made lowercase.
    type_description = models.CharField(db_column='Type_description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaction_details = models.CharField(db_column='Transaction_Details', max_length=45, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaction_id = models.CharField(db_column='Transaction_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usd_amount = models.DecimalField(db_column='USD_AMOUNT', max_digits=65, decimal_places=2)  # Field name made lowercase.
    transaction_date = models.DateTimeField(db_column='Transaction_date', blank=True, null=True)  # Field name made lowercase.
    eur_amount = models.CharField(db_column='EUR_AMOUNT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    is_ftd = models.CharField(max_length=45, blank=True, null=True)
    transaction_comment = models.CharField(max_length=45, blank=True, null=True)
    affiliate_id = models.CharField(max_length=45, blank=True, null=True)
    coupon = models.CharField(db_column='Coupon', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaction_time = models.DateTimeField(blank=True, null=True)
    created_time = models.DateTimeField(primary_key=True)
    source = models.CharField(db_column='SOURCE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    unique_id = models.CharField(max_length=45, blank=True, null=True)
    gateway_name = models.CharField(db_column='GATEWAY_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tp_response = models.CharField(db_column='TP_RESPONSE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gateway_instance = models.CharField(db_column='GATEWAY_INSTANCE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    depositor = models.CharField(db_column='DEPOSITOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    account_number = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='ACCOUNT_NUMBER')  # Field name made lowercase.
    lead_source = models.CharField(max_length=45, blank=True, null=True)
    account_status_at_trx = models.CharField(max_length=45, blank=True, null=True)

    primary_key=True
    class Meta:
        managed = False
        db_table = 'FINANCIAL_STATEMENTS'
        unique_together = (('created_time', 'account_number', 'amount'),)


class TradingPlatformAccounts(models.Model):
    account_id = models.IntegerField(db_column='ACCOUNT_ID', primary_key=True)  # Field name made lowercase.
    account_name = models.CharField(db_column='Account_Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    account_type = models.CharField(db_column='Account_Type', max_length=4, blank=True, null=True)  # Field name made lowercase.
    platform_name = models.CharField(db_column='Platform_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=4, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase.
    trading_platform_group = models.CharField(db_column='Trading_Platform_Group', max_length=45, blank=True, null=True)  # Field name made lowercase.
    assigned_to = models.CharField(db_column='Assigned_To', max_length=45, blank=True, null=True)  # Field name made lowercase.
    assigned_to_id = models.IntegerField(db_column='Assigned_To_ID', blank=True, null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='Created_Time', blank=True, null=True)  # Field name made lowercase.
    modified_time = models.DateTimeField(db_column='Modified_Time', blank=True, null=True)  # Field name made lowercase.
    last_login = models.DateTimeField(db_column='Last_Login', blank=True, null=True)  # Field name made lowercase.
    leverage = models.IntegerField(db_column='Leverage', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    equity = models.DecimalField(db_column='Equity', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    margin = models.DecimalField(db_column='Margin', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    margin_level = models.DecimalField(db_column='Margin_Level', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    margin_free = models.DecimalField(db_column='Margin_Free', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pl = models.DecimalField(db_column='PL', max_digits=65, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    test_account = models.IntegerField(db_column='Test_Account', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRADING_PLATFORM_ACCOUNTS'


class Symbols(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    symbol_group = models.ForeignKey('SymbolsGroups', models.DO_NOTHING, db_column='symbol_group')

    class Meta:
        managed = False
        db_table = 'SYMBOLS'


    def __str__(self):
        return self.name

class SymbolsGroups(models.Model):
    description = models.CharField(max_length=40)
    id_symbol_group = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'SYMBOLS_GROUPS'

    def __str__(self):
        return self.description


class Tickets(models.Model):
    ticket = models.IntegerField(primary_key=True)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    openprice = models.CharField(max_length=45)
    closedprice = models.DecimalField(max_digits=10, decimal_places=6)
    opentime = models.DateTimeField(blank=True, null=True)
    closedtime = models.DateTimeField()
    symbol = models.ForeignKey(Symbols, models.DO_NOTHING, db_column='symbol')
    tpa = models.ForeignKey(TradingPlatformAccounts, models.DO_NOTHING, db_column='tpa')

    class Meta:
        managed = False
        db_table = 'TICKETS'
