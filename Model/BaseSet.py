#codin:utf-8
from selenium import webdriver
import unittest

class Helper(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(120)
        self.driver.get('http://10.8.4.77:8120/person/login?appkey=WMS4-ST')

    def tearDown(self):
        self.driver.quit()