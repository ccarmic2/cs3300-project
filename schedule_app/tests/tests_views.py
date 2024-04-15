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
        create_supply_url = reverse("supply-add")
        response = self.client.post(create_supply_url, {
            'name': f'{name}',
            'description': f'{desc}'
        })
    
        new_supply = SupplyTask.objects.get(id=2)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(new_supply.name, name)
        self.assertEquals(new_supply.description, desc)

