from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.mycontactform.com")

time.sleep(3)

ele=driver.find_element(By.CLASS_NAME,"btn_log")

"""
click
double click
right click
click hold and release
drag and drop
drag and drop by

Action chains
create the object for the action class
pass driver object input

"""

a=ActionChains(driver)
#a.click(ele).perform()
time.sleep(1)

#a.double_click(ele).perform()
time.sleep(1)

#a.context_click(ele).perform()  #RIGHT CLICK
time.sleep(1)

#a.move_to_element(ele).click(ele).perform()
time.sleep(1)

a.click_and_hold(ele).perform()
time.sleep(1)

driver.quit()

