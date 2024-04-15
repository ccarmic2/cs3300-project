from django.test import TestCase, Client
from django.urls import reverse
from schedule_app.models import CalendarDates, SupplyTask
import json


class TestViews(TestCase):

    def setUp(self):
        suppy = SupplyTask.objects.create(
            name="test supply",
            description="test desc"
        )



    def test_date_list_GET(self):
        #test client
        client = Client()
        #have test client go to the list page
        response = client.get(reverse('dates'))

        #test status code (200 for success), and template sent
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedule_app/calendardates_list.html')

    def test_create_supply_POST(self):
        name = 'second supply'
        desc = 'test desc 2'
        #get the url to create an object
        create_supply_url = reverse("supply-add")
        #send a test client response to create a new object
        response = self.client.post(create_supply_url, {
            'name': f'{name}',
            'description': f'{desc}'
        })
        #get the newly created object (id = 2 for this new object, will differ for you)
        new_supply = SupplyTask.objects.get(id=2)

        #test response code for client redirect
        self.assertEquals(response.status_code, 302)
        #test object creatation and if it matches the values entered
        self.assertEquals(new_supply.name, name)
        self.assertEquals(new_supply.description, desc)

