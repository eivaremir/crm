# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from base.models import Accounts
from base.models import TradingPlatformAccounts

from base.models import FinancialStatements
from base.models import Symbols
from base.models import SymbolsGroups
from base.models import Tickets





class Partners(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    lead_source = models.CharField(primary_key=True, max_length=45)
    default_profile = models.ForeignKey('PartnersProfiles', models.DO_NOTHING, db_column='default_profile', blank=True, null=True)
    account_number = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='account_number', blank=True, null=True)
    account_number = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='account_number', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PARTNERS'
        verbose_name_plural = "Partners"
        verbose_name = "Partner"

    def __str__(self):
        return self.lead_source

class PartnersLeadSourceTree(models.Model):
    lead_source = models.OneToOneField('Partners', models.CASCADE, db_column='lead_source', primary_key=True)
    master = models.ForeignKey('Partners', models.DO_NOTHING, db_column='master', blank=True, null=True,related_name="master") #models.CharField(unique=True, max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PARTNERS_LEAD_SOURCE_TREE'
        verbose_name_plural = "Schemas"
        verbose_name = "Schema"
    
    def __str__(self):
        return f"Master ({self.master}) >> Sub ({self.lead_source})"

class PartnersLeadSource(models.Model):
    lead_source = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'PARTNERS_LEAD_SOURCE'

class PartnersReferals(models.Model):
    lead_source = models.OneToOneField(Partners, models.DO_NOTHING, db_column='lead_source', primary_key=True)
    account = models.ForeignKey(TradingPlatformAccounts, models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_REFERALS'
        unique_together = (('lead_source', 'account'),)

        verbose_name_plural = "Referals"
        verbose_name = "Referal"

class PartnersPaidTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'PARTNERS_PAID_TYPES'
    
    def __str__(self):
        return self.description

class PartnersCommissions(models.Model):
    ticket = models.OneToOneField(Tickets, models.DO_NOTHING, db_column='ticket', primary_key=True)
    
    lead_source = models.ForeignKey(Partners, models.DO_NOTHING, db_column='lead_source')
    tpa = models.ForeignKey(TradingPlatformAccounts, models.DO_NOTHING, db_column='tpa')
    comission_type = models.ForeignKey('PartnersCommTypes', models.DO_NOTHING, db_column='comission_type', blank=True, null=True)
    symbol = models.ForeignKey(Symbols, models.DO_NOTHING, db_column='symbol', blank=True, null=True)
    id_rule = models.ForeignKey('PartnersProfileRules', models.DO_NOTHING, db_column='id_rule')
    accounting_date = models.DateTimeField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paid = models.ForeignKey('PartnersPaidTypes', models.DO_NOTHING, db_column='paid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PARTNERS_COMMISSIONS'
        unique_together = (('ticket', 'lead_source'),)
        verbose_name_plural = "Commissions"
        verbose_name = "Commission"
    

class PartnersFinancialStatements(models.Model):
    fs_id = models.AutoField(primary_key=True)
    fs_type = models.ForeignKey('PartnersFsTypes', models.DO_NOTHING, db_column='fs_type')
    accounting_date = models.DateTimeField()
    creation_date = models.DateTimeField()
    description = models.CharField(max_length=45, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.ForeignKey('PartnersPaidTypes', models.DO_NOTHING, db_column='paid')
    lead_source = models.ForeignKey(Partners, models.DO_NOTHING, db_column='lead_source', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PARTNERS_FINANCIAL_STATEMENTS'
        verbose_name_plural = "Financial Statements"
        verbose_name = "Financial Statement"

class PartnersFsTypes(models.Model):
    id_fs_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45)
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_FS_TYPES'
        verbose_name_plural = "Financial Statement Types"
        verbose_name = "Financial Statement Type"

    def __str__(self):
        return self.description

class PartnersCommTypes(models.Model):
    id_comm_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45)
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_COMM_TYPES'
        verbose_name_plural = "Commission Types"
        verbose_name = "Commission Type"
    
    def __str__(self):
        return self.description

class PartnersTransactionTypes(models.Model):
    id_trx_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_TRANSACTION_TYPES'

    def __str__(self):
        return self.description

class PartnersTransactions(models.Model):
    transactions_id = models.AutoField(primary_key=True)
    lead_source = models.ForeignKey(Partners, models.DO_NOTHING, db_column='lead_source')
    creation_date = models.DateTimeField()
    accounting_date = models.DateTimeField()
    description = models.CharField(max_length=100)
    amt = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.IntegerField()
    trx_type = models.ForeignKey(PartnersTransactionTypes, models.DO_NOTHING, db_column='trx_type')
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_TRANSACTIONS'



class PartnersProfiles(models.Model):
    id_profile = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PARTNERS_PROFILES'

        verbose_name_plural = "Profiles"
        verbose_name = "Profile"

    def __str__(self):
        return f"{self.id_profile} - {self.description}"

class PartnersRuleSymbols(models.Model):
    symbol = models.ForeignKey(Symbols, models.DO_NOTHING, db_column='symbol')
    id_rule = models.ForeignKey('PartnersProfileRules', models.DO_NOTHING, db_column='id_rule')
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_RULE_SYMBOLS'

        verbose_name_plural = "Rule Symbols"
        verbose_name = "Rule Symbol"

class PartnersProfileRules(models.Model):
    id_rule = models.AutoField(primary_key=True)
    id_profile = models.ForeignKey(PartnersProfiles, models.DO_NOTHING, db_column='id_profile')
    description = models.CharField(max_length=45, blank=True, null=True)
    id_symbol_group = models.ForeignKey(SymbolsGroups, models.DO_NOTHING, db_column='id_symbol_group', blank=True, null=True)
    has_individual_symbols =  models.BooleanField() #models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_PROFILE_RULES'

        verbose_name_plural = "Profile Rules"
        verbose_name = "Profile Rule"
    
    def __str__(self):
        return self.description

class PartnersRulesLevels(models.Model):
    id_rule = models.OneToOneField(PartnersProfileRules, models.DO_NOTHING, db_column='id_rule', primary_key=True)
    level = models.IntegerField()
    amt = models.CharField(max_length=45, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_RULES_LEVELS'
        unique_together = (('id_rule', 'level'),)

        verbose_name_plural = "Profile Rule Levels"
        verbose_name = "Profile Rule Level"

    def __str__():
        return f"{self.id_rule} #{self.level}"