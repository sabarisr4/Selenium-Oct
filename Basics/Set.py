from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(2)

driver.set_window_size(1200, 900)

driver.quit()