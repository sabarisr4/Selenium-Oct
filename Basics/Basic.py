from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)
c=driver.get_cookies()
print("number of cookies:",len(c))

driver.quit()



