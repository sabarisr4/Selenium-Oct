from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com/")

#Alert notification
#driver.execute_script("alert('Hello World!');")

#Window confirm

driver.execute_script("window.confirm('Hello World!');")
time.sleep(3)
f=driver.switch_to.alert
f.accept()

driver.quit()


