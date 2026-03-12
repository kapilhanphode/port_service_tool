from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "user_type"]
    search_fields = ["name", "email", "user_type"]
    list_filter = ["user_type"]
