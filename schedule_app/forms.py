from django.forms import ModelForm
from .models import CalendarDates, SupplyTask


class DateForm(ModelForm):
    class Meta:
        model = CalendarDates
        fields = '__all__'


class SupplyForm(ModelForm):
    class Meta:
        model = SupplyTask
        fields = '__all__'
