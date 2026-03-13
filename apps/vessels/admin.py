from django.contrib import admin
from .models import Vessel
from apps.core.admin_site import port_admin

@admin.register(Vessel, site=port_admin)
# @admin.register(Vessel)
class VesselAdmin(admin.ModelAdmin):
    list_display = ('name', 'vessel_type', 'company')
    search_fields = ('name',)
    list_filter = ('vessel_type',)
