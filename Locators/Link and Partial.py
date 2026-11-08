from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com")

driver.find_element(By.LINK_TEXT,"Privacy").click()   #LINK TEXT
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"Pri").click()  #PARTIAL LINK TEXT
time.sleep(3)

driver.quit()