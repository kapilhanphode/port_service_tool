from django.contrib import admin
from .models import User
from apps.core.admin_site import port_admin

@admin.register(User, site=port_admin)
# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "user_type"]
    search_fields = ["name", "email", "user_type"]
    list_filter = ["user_type"]
