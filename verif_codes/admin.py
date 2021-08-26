from django.contrib import admin

#from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from verif_codes.models import VerificationCodes
from verif_codes.models import ParamsVerificationEntityTypes
from verif_codes.models import ParamsVerificationCodeTypes
from django.contrib.auth.models import User





@admin.register(VerificationCodes)
class VerificationCodesAdmin(admin.ModelAdmin):
    
    list_display = ('code','code_type','identity','entity_type','expiration_date')
    #list_display_links = ('code','identity')
    verbose_name = "Verification Codes"
    list_filter = ('entity_type','code_type')
    search_fields = ('code','identity')
    list_editable = ('identity',)
    readonly_fields = ('entity_type','code_type')


@admin.register(ParamsVerificationEntityTypes)
class ParamsVerificationEntityTypesAdmin(admin.ModelAdmin):
    
    #list_display = ('code','code_type','identity','entity_type','expiration_date')
    #list_display_links = ('code','identity')
    verbose_name = "Entity Codes"
    #list_filter = ('entity_type','code_type')
    search_fields = ('description',)
    #list_editable = ('identity',)
    #readonly_fields = ('entity_type','description')

@admin.register(ParamsVerificationCodeTypes)
class ParamsVerificationCodeTypesAdmin(admin.ModelAdmin):
    
    #list_display = ('code','code_type','identity','entity_type','expiration_date')
    #list_display_links = ('code','identity')
    verbose_name = "Verification Code Types"
    #list_filter = ('entity_type','code_type')
    search_fields = ('description',)
    #list_editable = ('identity',)
    #readonly_fields = ('entity_type','description')





admin.site.site_header = "ZumaMarkets"