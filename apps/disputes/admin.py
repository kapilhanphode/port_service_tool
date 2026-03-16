from django.contrib import admin
from .models import Dispute
from apps.core.admin_site import port_admin


@admin.register(Dispute, site=port_admin)
class DisputeAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'raised_by', 'status')
    list_filter = ('status',)
    search_fields = ('order', 'raised_by', 'status')

