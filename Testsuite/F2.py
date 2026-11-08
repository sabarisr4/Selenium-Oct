import unittest

from selenium import webdriver

from selenium.webdriver.common.by import By


class Two(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        print(cls)
        global driver
        print("setup class :  visiting the website ")


        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.bing.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_count(self):
        print("Test case : counting ")
        print(len(self.driver.find_elements(By.TAG_NAME,"a")))