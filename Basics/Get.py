import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.google.com")

print(driver.get_window_size())
print(driver.get_window_position())
print(driver.get_cookies())
print(driver.title)
print(driver.current_url)

time.sleep(2)

driver.quit()

