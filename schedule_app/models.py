from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.


class CalenderDates(models.Model):
    DEFAULT_TIME = "10:00"

    booking_start = models.DateField()
    booking_end = models.DateField()
    checkout_time = models.TimeField(DEFAULT_TIME)
    notes = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.booking_end)

    def get_absolute_url(self):
        return reverse("date_detail", args=[str(self.id)])


class SupplyTask(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("supply_detail", args=[str(self.id)])
