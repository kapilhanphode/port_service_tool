from django.contrib import admin
from .models import RFQ
from apps.core.admin_site import port_admin


@admin.register(RFQ, site=port_admin)
class RFQAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'service', 'status')
    search_fields = ['title', 'company']
    list_filter = ('status', 'service', 'is_deleted')
