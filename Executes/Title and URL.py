from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(3)


print(driver.execute_script("return document.title"))

print(driver.execute_script("return document.URL"))

driver.quit()
