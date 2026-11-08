import time
import unittest

from selenium import webdriver



class Three(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        print(cls)
        global driver
        print("setup class :  visiting the website ")


        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.facebook.com")


    @classmethod
    def tearDownClass(cls) :
        time.sleep(4)
        cls.driver.quit()

    def test_resi(self):
        print("Test case : resizing")
        self.driver.set_window_size(100,200)