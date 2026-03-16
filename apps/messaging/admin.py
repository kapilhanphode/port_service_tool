from django.contrib import admin
from .models import Message
from apps.core.admin_site import port_admin

@admin.register(Message, site=port_admin)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'rfq')
    search_fields = ('subject', 'rfq')
    list_filter = ('subject', 'rfq')

