from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(2)

driver.maximize_window()
time.sleep(2)
#driver.minimize_window()
time.sleep(2)

for i in range(1):
    driver.refresh()

time.sleep(2)
driver.quit()

