from django.db import models
from django.urls import reverse
from datetime import time

# Create your models here.


class CalendarDates(models.Model):
    DEFAULT_TIME = time(hour=10, minute=0)

    booking_start = models.DateField()
    booking_end = models.DateField()
    checkout_time = models.TimeField(default=DEFAULT_TIME)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        print(self.booking_end)
        return str(self.booking_end)

    def get_absolute_url(self):
        return reverse("date-detail", args=[str(self.id)])


class SupplyTask(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("supply-detail", args=[str(self.id)])

#class Usersysmanager(BaseUserManager):
#    def create_user(self, username, email, password=None, role='cleaner'):
#       if not email:
#            raise ValueError('User must have an email address')
#            
#        user = self.model(
#            email=self.normalize_email(email)
#
#        )