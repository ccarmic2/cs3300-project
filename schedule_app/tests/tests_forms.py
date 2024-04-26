from django.test import TestCase
from schedule_app.forms import DateForm, SupplyForm, CreateUserForm
from datetime import date, time

class TestDateForms(TestCase):
    #test a valid form
    def test_vaild_date(self):
        form = DateForm(data={
            'booking_start': date(2024, 9, 27),
            'booking_end': date(2024, 10, 5),
            'checkout_time': time(hour=10, minute=30),
            'description': 'tests desc'
        })

        self.assertTrue(form.is_valid())

    #test a form with no data entered
    def test_no_data(self):
        form = DateForm(data={})

        self.assertFalse(form.is_valid())
        #makes sure that there are 4 errors (one error for each blank field)
        self.assertEquals(len(form.errors), 3)
    
