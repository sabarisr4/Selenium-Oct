from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.mycontactform.com")


time.sleep(3)

driver.find_element(By.ID,"user").send_keys("Dhivyakarthi123")  #ID
time.sleep(3)

driver.find_element(By.NAME,"pass").send_keys("12345")  #NAME
time.sleep(3)

driver.find_element(By.CLASS_NAME,"btn_log").click()  #CLASS NAME
time.sleep(3)

driver.quit()