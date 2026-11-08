import unittest

from selenium import webdriver

from selenium.webdriver.common.by import By


class First(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        print(cls)
        global driver  #global variable
        print("setup class :  visiting the website ")


        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.google.com")



    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()


    def test_clicking(self):
        print("Test case : clicking ")
        self.driver.find_element(By.LINK_TEXT,"Images").click()

