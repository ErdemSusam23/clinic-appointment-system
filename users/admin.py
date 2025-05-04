from django.contrib import admin
from appointments.models import Appointment
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'date_of_birth')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('role',)


