from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(3)


l=driver.find_elements(By.TAG_NAME,"img")   #collection of images
print("number of images:",len(l))

v=driver.find_elements(By.TAG_NAME,"a") #collection of links
print("number of links:",len(v))

e=driver.find_elements(By.TAG_NAME,"div")  #collection of div
print("number of elements in div:",len(e))

time.sleep(1)
driver.quit()