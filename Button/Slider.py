from selenium import webdriver

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")
time.sleep(3)

"""

frame - iframe
elements -  inside frame
switch ur control to frame
id,name,index
"""


driver.switch_to.frame(0)
ac=ActionChains(driver)

e=driver.find_element(By.ID, "slider")
ac.drag_and_drop_by_offset(e,50,0).perform()
time.sleep(2)
driver.quit()