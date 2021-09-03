from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from partners.models import Partners
from partners.models import PartnersReferals
from partners.models import PartnersCommissions
from partners.models import PartnersFinancialStatements
from partners.models import PartnersFsTypes
from partners.models import PartnersCommTypes
from partners.models import PartnersTransactionTypes
from partners.models import PartnersTransactions
from partners.models import PartnersProfiles
from partners.models import PartnersRuleSymbols
from partners.models import PartnersProfileRules
from partners.models import PartnersRulesLevels


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    
    list_display = ('lead_source','balance','master','default_profile')
    #list_display_links = ('code','identity')
    verbose_name = "Partners"
    list_filter = ('lead_source',)
    search_fields = ('default_profile',)
    list_editable = ('default_profile','master')
    #readonly_fields = ('entity_type','code_type')


@admin.register(PartnersTransactions)
class PartnerTransactionsAdmin(admin.ModelAdmin):
    
    list_display = ('transactions_id','lead_source','amt','paid')
    #list_display_links = ('code','identity')
    verbose_name = "Partners Transactions"
    list_filter = ('lead_source','paid')
    search_fields = ('lead_source','amt')
    #list_editable = ('lead_source','default_profile')
    #readonly_fields = ('entity_type','code_type')