from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from django.contrib.auth.models import User, Group
from ..models import CalendarDates, SupplyTask

from django.test import TestCase, Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IntegrateTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.cleaner_group = Group(name='cleaner_role')
        cls.cleaner_group.save()
        cls.owner_group = Group(name='owner_role')
        cls.owner_group.save()
        test_user = User.objects.create_user(username='test_user',
                                             email='test_user@test.com',
                                             password="rJNL7b5Y$3GdEe")
        test_user.groups.add(cls.owner_group)
        cls.browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        self.c = Client()
        self.dates_url = reverse('dates')
        self.create_dates_url = reverse('date-add')
        self.supplies_url = reverse('supplies')
        self.create_supply_url = reverse('supply-add')
        super(IntegrateTest, self).setUp()
        login = self.c.login(username='test_user', password='rJNL7b5Y$3GdEe')
        cookie = self.c.cookies['sessionid']
        self.browser.get(self.live_server_url)
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
    
    def test_create_date_button(self):
        wait = WebDriverWait(self.browser, 5)
        self.browser.get(self.live_server_url + self.dates_url)
        elem = wait.until(
            EC.element_to_be_clickable((By.ID, 'add-b'))
        )
        elem.click()
        self.assertEqual(self.browser.current_url, self.live_server_url + self.create_dates_url)
    
    def test_create_supply(self):
        wait = WebDriverWait(self.browser, 5)
        self.browser.get(self.live_server_url + self.supplies_url)
        elem = wait.until(
            EC.element_to_be_clickable((By.ID, 'add-b'))
        )
        elem.click()
        self.assertEqual(self.browser.current_url, self.live_server_url + self.create_supply_url)
    
    def test_home_next(self):
        wait = WebDriverWait(self.browser, 5)
        self.browser.get(self.live_server_url)
        elem = wait.until(
            EC.element_to_be_clickable((By.ID, 'next-b'))
        )
        elem.click()
        self.assertNotEqual(self.browser.current_url, self.live_server_url)

    def test_home_prev(self):
        wait = WebDriverWait(self.browser, 5)
        self.browser.get(self.live_server_url)
        elem = wait.until(
            EC.element_to_be_clickable((By.ID, 'prev-b'))
        )
        elem.click()
        self.assertNotEqual(self.browser.current_url, self.live_server_url)   

        



