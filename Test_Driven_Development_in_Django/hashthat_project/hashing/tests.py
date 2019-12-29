from django.test import TestCase
from selenium import webdriver


class FunctionalTestCase(TestCase):
    def setUp(self):
        browser = webdriver.Chrome()
        browser.get('http://localhost:8000')
        assert browser.page_source.find('install')
