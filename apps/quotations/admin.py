from django.contrib import admin
from .models import Quotation
from apps.core.admin_site import port_admin

@admin.register(Quotation, site=port_admin)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'rfq', 'supplier_company', 'price', 'status')
    list_filter = ('status', 'rfq', 'is_deleted')
    search_fields = ('rfq', 'supplier_company')

