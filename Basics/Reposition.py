from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(2)

driver.set_window_rect(0, 0, 800, 600)

time.sleep(2)

driver.quit()