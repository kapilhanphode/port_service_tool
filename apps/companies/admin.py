from django.contrib import admin
from .models import Company
from apps.core.admin_site import port_admin

@admin.register(Company, site=port_admin)
# @admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company_type')
    fields = ('name', 'company_type', 'country', 'city', 'imo_company_number', 'verified', 'created_by')
    list_filter = ('company_type',)
    search_fields = ('name',)
