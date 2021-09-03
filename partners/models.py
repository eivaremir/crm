# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from crm.models import Accounts
from crm.models import TradingPlatformAccounts

from crm.models import FinancialStatements
from crm.models import Symbols
from crm.models import SymbolsGroups
from crm.models import Tickets

class Partners(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    lead_source = models.CharField(primary_key=True, max_length=45)
    default_profile = models.ForeignKey('PartnersProfiles', models.DO_NOTHING, db_column='default_profile', blank=True, null=True)
    master = models.CharField(max_length=45, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'PARTNERS'

class PartnersReferals(models.Model):
    lead_source = models.OneToOneField(Partners, models.DO_NOTHING, db_column='lead_source', primary_key=True)
    account = models.ForeignKey(TradingPlatformAccounts, models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_REFERALS'
        unique_together = (('lead_source', 'account'),)

class PartnersCommissions(models.Model):
    ticket = models.OneToOneField(Tickets, models.DO_NOTHING, db_column='ticket', primary_key=True)
    transaction = models.ForeignKey('PartnersTransactions', models.DO_NOTHING)
    lead_source = models.CharField(max_length=45)
    tpa = models.ForeignKey(TradingPlatformAccounts, models.DO_NOTHING, db_column='tpa')
    comission_type = models.ForeignKey('PartnersCommTypes', models.DO_NOTHING, db_column='comission_type')
    symbol = models.ForeignKey(Symbols, models.DO_NOTHING, db_column='symbol')
    id_rule = models.ForeignKey('PartnersProfileRules', models.DO_NOTHING, db_column='id_rule')
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_COMMISSIONS'

class PartnersFinancialStatements(models.Model):
    transaction = models.OneToOneField('PartnersTransactions', models.DO_NOTHING, primary_key=True)
    fs_type = models.ForeignKey('PartnersFsTypes', models.DO_NOTHING, db_column='fs_type')
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_FINANCIAL_STATEMENTS'

class PartnersFsTypes(models.Model):
    id_fs_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45)
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_FS_TYPES'

class PartnersCommTypes(models.Model):
    id_comm_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45)
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_COMM_TYPES'

class PartnersTransactionTypes(models.Model):
    id_trx_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_TRANSACTION_TYPES'

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
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_PROFILES'

class PartnersRuleSymbols(models.Model):
    symbol = models.ForeignKey(Symbols, models.DO_NOTHING, db_column='symbol')
    id_rule = models.ForeignKey('PartnersProfileRules', models.DO_NOTHING, db_column='id_rule')
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_RULE_SYMBOLS'

class PartnersProfileRules(models.Model):
    id_rule = models.IntegerField(primary_key=True)
    id_profile = models.ForeignKey(PartnersProfiles, models.DO_NOTHING, db_column='id_profile')
    description = models.CharField(max_length=45, blank=True, null=True)
    id_symbol_group = models.ForeignKey(SymbolsGroups, models.DO_NOTHING, db_column='id_symbol_group', blank=True, null=True)
    has_individual_symbols = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_PROFILE_RULES'

class PartnersRulesLevels(models.Model):
    id_rule = models.OneToOneField(PartnersProfileRules, models.DO_NOTHING, db_column='id_rule', primary_key=True)
    level = models.IntegerField()
    amt = models.CharField(max_length=45, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'PARTNERS_RULES_LEVELS'
        unique_together = (('id_rule', 'level'),)