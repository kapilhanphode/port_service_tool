from django.contrib import admin
from .models import Service
from apps.core.admin_site import port_admin

@admin.register(Service, site=port_admin)
# @admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    search_fields = ('name',)
    list_filter = ('name',)
