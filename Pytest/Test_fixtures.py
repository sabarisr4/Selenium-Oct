#Function Level

"""
fixtures:class level,function level

setupclass:only once before test cases
teardown class:only after  all test cases

setup:before test case run
teardown:after test case run

yield - run after test case execution
"""
import pytest
from selenium import webdriver

import time



from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    print("executing each test cases")
    global driver

    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    yield
    print("executing after test cases")
    time.sleep(2)
    driver.close()


def test_title(setup):
    print("testcase1:getting title")
    print(driver.title)

def test_clicking(setup):
    driver.find_element(By.LINK_TEXT, "Images").click()
