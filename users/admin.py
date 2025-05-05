from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from appointments.models import Appointment
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'date_of_birth')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('role',)
    
    # Add these fields from BaseUserAdmin
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'date_of_birth')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('first_name', 'last_name', 'role', 'date_of_birth')}),
    )


