from selenium import webdriver

import time

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
time.sleep(3)


time.sleep(3)

driver.find_element(By.ID, "bmwradio").click()
time.sleep(1)
driver.find_element(By.ID, "benzradio").click()
time.sleep(1)
driver.find_element(By.ID, "hondaradio").click()
driver.quit()