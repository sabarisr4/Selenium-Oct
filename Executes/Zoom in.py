from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(2)
#zoom in and zoom out
#grater than 100 zoom in
#less than 100 zoom out
#100:normal

driver.execute_script("document.body.style.zoom=140")
time.sleep(2)
driver.execute_script("document.body.style.zoom=70")
time.sleep(2)
driver.execute_script("document.body.style.zoom=100")
time.sleep(2)

driver.quit()
