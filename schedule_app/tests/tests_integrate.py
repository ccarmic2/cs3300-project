from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from django.contrib.auth.models import User, Group
from ..models import CalendarDates, SupplyTask

from django.test import TestCase
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
        test_user.groups.add(cls.cleaner_group)
        cls.browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        self.dates_url = reverse('dates')
        self.create_dates_url = reverse('date-add')
        self.supplies_url = reverse('supplies')
        self.create_supply_url = reverse('supply-add')
        super(IntegrateTest, self).setUp
        ...
    
    def test_create_date(self):
        self.browser.get(self.live_server_url + self.dates_url)
        title = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn btn-primary'))
        )
        print(self.live_server_url, self.dates_url)
        self.assertEqual(self.live_server_url, self.dates_url)

        ...


