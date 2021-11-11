from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(label="Date", widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username','birth_date', 'mobile_number', 'aadhar_number',)

class CustomUserChangeForm(UserChangeForm):
    birth_date = forms.DateField(label="Date", widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username', 'birth_date', 'mobile_number', 'aadhar_number',)