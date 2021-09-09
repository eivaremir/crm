from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.db import models

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
from partners.models import PartnersLeadSourceTree




@admin.register(PartnersFsTypes)
class PartnersFsTypesAdmin(admin.ModelAdmin):
    list_display = ('id_fs_type','description')
    search_fields = ('description',)
    list_editable = ('description',)
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(PartnersCommTypes)
class PartnerCommissionTypesAdmin(admin.ModelAdmin):
    list_display = ('id_comm_type','description')
    search_fields = ('description',)
    list_editable = ('description',)
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(PartnersFinancialStatements)
class PartnersFinancialStatementsAdmin(admin.ModelAdmin):
    list_display = ('fs_id','lead_source','fs_type','amount','paid','accounting_date','creation_date','description')
    search_fields =('fs_id','lead_source','fs_type','amount','paid','accounting_date','creation_date','description')
    list_editable = ('lead_source','paid','accounting_date','creation_date')
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PartnersCommissions)
class PartnersCommissionsAdmin(admin.ModelAdmin):
    list_display = ('ticket','tpa','lead_source','amount','paid','symbol','id_rule','accounting_date','creation_date')
    search_fields =('ticket','lead_source','amount','paid','accounting_date','creation_date','description')
    list_editable = ('lead_source','paid','accounting_date','creation_date')
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    
    list_display = ('lead_source','account_number','balance','default_profile')
    #list_display_links = ('code','identity')
    verbose_name = "Partners"
    list_filter = ('lead_source',)
    search_fields = ('default_profile',)
    list_editable = ('default_profile','account_number')
    #readonly_fields = ('entity_type','code_type')


@admin.register(PartnersProfiles)
class PartnerProfileAdmin(admin.ModelAdmin):
    
    list_display = ('id_profile','description')
    search_fields = ('description',)
    #list_display_links = ('',)
    list_editable = ('description',)
    #verbose_name = "Partner Levels"
    

@admin.register(PartnersLeadSourceTree)
class PartnerTreeAdmin(admin.ModelAdmin):
    
    list_display = ('lead_source','master')
    search_fields = ('lead_source__balance',)
    #list_display_links = ('',)
    list_editable = ('master',)
    verbose_name = "Partner Levels"
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(PartnersProfileRules)
class PartnersProfileRulesAdmin(admin.ModelAdmin):
    
    list_display = ('id_rule','description','id_profile','id_symbol_group','has_individual_symbols')
    search_fields = ('description','id_profile','id_symbol_group')
    #list_display_links = ('',)
    list_editable = ('has_individual_symbols',)
    #list_filter = ('id_symbol_group__symbol',)
    
    
@admin.register(PartnersRulesLevels)
class PartnersRulesLevelsAdmin(admin.ModelAdmin):
    
    list_display = ('id_rule','level','amt')
    search_fields = ('id_rule',)
    #list_display_links = ('',)
    list_editable = ('amt','level')


"""
class PartnersInline(admin.StackedInline):
    model = PartnersLeadSourceTree
    can_delete = False
    verbose_name_plural = 'Trees'
    
    
class PartnerAdmin(Partners):
    inlines = (PartnersInline,)
    list_display = (
        'lead_source',
        'balance'
    )
    
admin.site.unregister(Partners)
admin.site.register(Partners, PartnerAdmin)"""