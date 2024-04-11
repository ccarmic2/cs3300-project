from django.test import TestCase
from models import CalendarDates, SupplyTask

class CalendarDatesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CalendarDates.objects.create()
        ...

    def setUp(self):
        ...

    def test_false_is_false(self):
        ...

    def test_false_is_true(self):
        ...

    def test_one_plus_one_equals_two(self):
        ...
    
class SupplyTaskTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        SupplyTask.objects.create(name="Test Task", description="test desc")
        ...

    def setUp(self):
        ...

    def test_name_max_length(self):
        task = SupplyTask.objects.get(id=1)
        max_length = task._meta.get_field('name').max_length
        self.assertEqual(max_length, 150)

    def test_description_max_length(self):
        task = SupplyTask.objects.get(id=1)
        max_length = task._meta.get_field('description').max_length
        self.assertEqual(max_length, 250)

    def test_one_plus_one_equals_two(self):
        ...
    
