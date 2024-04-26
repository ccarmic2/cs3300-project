from sqlite3 import DatabaseError
from django.contrib.auth.models import User, Group
from django.test import TestCase, Client
from django.urls import reverse
from schedule_app.models import CalendarDates, SupplyTask
import json


class TestViewsModels(TestCase):
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
        create_supply_url = reverse('supply-add')
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
    
class TestViewsUsers(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cleaner_group = Group(name='cleaner_role')
        cls.cleaner_group.save()
        cls.owner_group = Group(name='owner_role')
        cls.owner_group.save()
        test_user = User.objects.create_user(username='test_user',
                                             email='test_user@test.com',
                                             password="rJNL7b5Y$3GdEe")
        test_user.groups.add(cls.cleaner_group)

    def setUp(self):
        self.c = Client()
        self.register_url = reverse('register_page')
        self.login_url = reverse('login')
        self.cleaner_group = Group.objects.get(name='cleaner_role')
        self.owner_group = Group.objects.get(name='owner_role')
        self.user_reg = {
            'email':'test.user.1@test.com',
            'username':'test_user_1',
            'password1':'@65QPH8b$r%TV6',
            'password2':'@65QPH8b$r%TV6',
        }
        self.user_log = {
            'username':'test_user',
            'password':'rJNL7b5Y$3GdEe',
        }

    def test_register_page(self):
        response = self.c.post(self.register_url, self.user_reg)
        self.assertEqual(response.status_code, 302)
    
    def test_login(self):
        response = self.c.post(self.login_url, self.user_log)
        self.assertEqual(response.status_code, 302)

