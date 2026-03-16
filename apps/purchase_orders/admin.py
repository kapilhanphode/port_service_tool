from django.contrib import admin
from .models import PurchaseOrder
from apps.core.admin_site import port_admin

@admin.register(PurchaseOrder, site=port_admin)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'quotation', 'supplier_company', 'total_amount', 'status')
    list_filter = ('status',)
    search_fields = ('quotation', 'supplier_company', 'status')

