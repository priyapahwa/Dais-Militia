from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_from = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'birth_date', 'mobile_number', 'aadhar_number']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('birth_date', 'mobile_number', 'aadhar_number')}),)

admin.site.register(CustomUser, CustomUserAdmin)