from django.test import TestCase
from selenium import webdriver


class FunctionalTestCase(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_homepage_exists(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('install', self.browser.page_source)

    def test_hash_of_hello(self):
        self.browser.get('http://localhost:8000')
        text = self.browser.find_element_by_id('id_text')
        text.send_keys('hello')
        self.browser.find_element_by_name('submit').click()
        self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161',
                      self.browser.page_source)

    def tearDown(self):
        self.browser.quit()
