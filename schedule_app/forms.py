from django.forms import ModelForm, Form
from django import forms
from .models import CalendarDates, SupplyTask
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DateForm(ModelForm):
    class Meta:
        model = CalendarDates
        fields = '__all__'


class SupplyForm(ModelForm):
    class Meta:
        model = SupplyTask
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
