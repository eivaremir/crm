from django.contrib import admin

#from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Accounts
from .models import FinancialStatements
from .models import Symbols
from .models import SymbolsGroups
from .models import Tickets
from .models import BaseParams
from .models import BaseSalesAgents
from .models import BaseSalesOffices
#from django.contrib.auth.models import User

@admin.register(FinancialStatements)
class FinancialStatementsAdmin(admin.ModelAdmin):
    list_display = ('tpa','type_description','depositor','usd_amount','real_amount','is_real','created_time')
    search_fields = ('tpa','type_description')
    list_filter = ('type_description','depositor')
    list_editable = ('is_real',)

@admin.register(BaseSalesAgents)
class BaseSalesAgentsAdmin(admin.ModelAdmin):
    list_display = ('name','office','list_in_reports')
    search_fields = ('name','office')
    list_filter = ('office',)
    list_editable = ('office','list_in_reports')

@admin.register(BaseSalesOffices)
class BaseSalesOfficesAdmin(admin.ModelAdmin):
    list_display = ('code','description')
    search_fields = ('code','description')

@admin.register(BaseParams)
class BaseParamsAdmin(admin.ModelAdmin):
    list_display = ('param','value')
    search_fields = ('value','param')
    list_editable = ('value',)
    


@admin.register(Symbols)
class SymbolsAdmin(admin.ModelAdmin):
    
    list_display = ('name','symbol_group')
    
    
    list_filter = ('symbol_group',)
    search_fields = ('name','symbol_group')
    list_editable = ('symbol_group',)
    #readonly_fields = ('account_number',)


@admin.register(SymbolsGroups)
class SymbolsGroupsAdmin(admin.ModelAdmin):
    list_display = ('id_symbol_group','description')
    list_filter = ('description',)
    search_fields = ('id_symbol_group','description')
    list_editable = ('description',)
    #readonly_fields = ('account_number',)

@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    
    list_display = ('account_number','account_name','primary_email','created_time','assigned_to','lead_source','country')
    list_display_links = ('account_number',)
    
    #list_filter = ('entity_type','code_type')
    search_fields = ('account_name','primary_email','lead_source','country')
    list_editable = ('lead_source','primary_email')
    readonly_fields = ('account_number',)


admin.site.site_header = "ZumaMarkets"



