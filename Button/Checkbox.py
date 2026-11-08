from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")

time.sleep(3)

""""
create an object for class
pass dropdown box as input
select the options
index
value
visible text
only one option selected

"""

ele=driver.find_element(By.ID,"checkbox-example-div")
s=Select(ele)

#s.select_by_index(1)
time.sleep(1)

s.select_by_value("bmw")
time.sleep(1)

#s.select_by_visible_text("Honda")
time.sleep(1)
driver.quit()
