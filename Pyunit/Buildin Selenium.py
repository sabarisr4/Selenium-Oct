
"""
setupclass:only once before all the test cases started execution
tear down class:only once after all the test cases execution

setup:run before every test case
teardown:run after every test case

setupclass
  setup tc1 teardown
  setup tc2 teardown
  setup tc3 teardown
  setup tc4 teardown

tear down class

"""






import unittest

import HtmlTestRunner

from HtmlTestRunner import HTMLTestRunner

from openpyxl.styles.builtins import title
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("before all test cases")
        global driver

        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.google.com")
    @classmethod
    def tearDownClass(cls):
        print("after all test cases")
        cls.driver.quit()

    def setUp(self):
        print("before each")
        self.driver.refresh()

    def tearDown(self):
        print("after each")
        print(len(self.driver.get_cookies()))


    def test_1(self):
        print("test case 1")
        self.driver.find_element(By.LINK_TEXT, "Terms")

    def test_2(self):
        print("test case 2")
        print(self.driver.title)



if __name__=='__main__':
    unittest.main(testRunner=HTMLTestRunner(open_in_browser=True, output='sabari.html'))

#Visit the google
#refresh
#click terms
#get cookies
#refresh
#get title
#get cookies
#quit

