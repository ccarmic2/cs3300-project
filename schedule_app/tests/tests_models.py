from django.test import TestCase
from schedule_app.models import CalendarDates, SupplyTask

class CalendarDatesTest(TestCase):
    @classmethod
    def setUp(self):
        self.dates = CalendarDates.objects.create(
            booking_start='2024-10-05',
            booking_end='2024-10-10'
        )

    def test_description_max_length(self):
        max_length = self.dates._meta.get_field('description').max_length
        self.assertEqual(max_length, 500)

    def test_date_url(self):
        date_url = f'/dates/{self.dates.id}'
        self.assertEqual(self.dates.get_absolute_url(), date_url)

    
class SupplyTaskTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        SupplyTask.objects.create(name="Test Task", description="test desc")

    def test_name_max_length(self):
        task = SupplyTask.objects.get(id=1)
        max_length = task._meta.get_field('name').max_length
        self.assertEqual(max_length, 150)

    def test_description_max_length(self):
        task = SupplyTask.objects.get(id=1)
        max_length = task._meta.get_field('description').max_length
        self.assertEqual(max_length, 250)

