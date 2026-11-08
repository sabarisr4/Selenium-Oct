from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")
time.sleep(3)

"""
conditional,unconditional
unconditional - implicit wait
once it is declared all the code which is present after it will take the time limit

code is correct  - executes within the time limit ,it will proceed further ,it will not wait completion of time limit
code is incorrect  - it will  wait completion of time limit

"""
driver.implicitly_wait(5)
print(driver.title)
time.sleep(3)

c=driver.get_cookies()
print("number of cookies",len(c))
time.sleep(3)

driver.refresh()

driver.quit()

time.sleep(3)