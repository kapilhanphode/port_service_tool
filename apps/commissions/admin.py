from django.contrib import admin
from .models import Commission
from apps.core.admin_site import port_admin

@admin.register(Commission, site=port_admin)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'commission_amount', 'commission_percentage')
    search_fields = ('order', 'description')
    list_filter = ('order',)

