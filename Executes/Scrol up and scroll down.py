from selenium import webdriver


import time


driver=webdriver.Chrome()
driver.get("https://www.letskodeit.com/")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight);")

time.sleep(3)

driver.quit()
