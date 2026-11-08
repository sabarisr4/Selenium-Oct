from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(3)


"""
time limit - particular condition
create and object for webdriver wait class
pass driver instance and time limit as input
call until
call condition

"""

w=WebDriverWait(driver,5)
#Full title
#w.until(expected_conditions.title_is("yahoo"))

#Half title
#w.until(expected_conditions.title_is("yah"))

#Alert
#w.until(expected_conditions.alert_is_present())

#Visibility of single element
#w.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "images")))

#Visibility of all element
#w.until(expected_conditions.visibility_of_all_elements_located((By.TAG_NAME, "img")))


w.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Gmail")))


driver.save_screenshot("SR.Png")
driver.quit()