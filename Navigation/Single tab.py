#Single tab with forward and backward

from selenium import webdriver
import time


from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.google.com")

time.sleep(3)

driver.find_element(By.LINK_TEXT, "Privacy").click()

time.sleep(3)

driver.forward()

time.sleep(3)

driver.back()

time.sleep(3)

driver.quit()

