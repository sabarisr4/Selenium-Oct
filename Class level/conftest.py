from selenium import webdriver

from selenium.webdriver.chrome.service import Service

#logging - replace of printing

#setup(before yield) class (functions)   setup(after yield)

import pytest
import logging #create the logfile

#info,debug,error,warning,critical

#info:info,error,warning,critical
#debug:all message
#error:error and critical message
#warning:error,warning and critical message
#critical :critical message

logging.basicConfig(
    level=logging.DEBUG,
    filename="sabari.log",
    filemode="a",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%Y-%H:%M:%S')

@pytest.fixture(scope="class")
def setup(request):

    logging.info("Initializing Chrome driver")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")

    request.cls.driver = driver

    logging.info("Visiting website")

    yield driver

    logging.info("Closing browser")
    driver.quit()