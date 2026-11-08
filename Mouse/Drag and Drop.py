from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://jqueryui.com/droppable/")

time.sleep(3)

"""

frame - iframe
elements -  inside frame
switch ur control to frame
id,name,index

"""

driver.switch_to.frame(0)
obj=ActionChains(driver)

e1=driver.find_element(By.ID,"draggable")
e2=driver.find_element(By.ID,"droppable")

obj.drag_and_drop(e1,e2).perform()
time.sleep(3)
driver.quit()

