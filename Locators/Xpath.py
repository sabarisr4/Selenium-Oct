from selenium import webdriver
import time

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.mycontactform.com")
time.sleep(3)

#xpath - xml path language
#1.absolute xpath - copy full xpath
#2.relative xpath - copy xpath


#absolute xpath - copy full xpath
driver.find_element(By.XPATH,"//html//body//div[3]//div[2]//div[1]//form//fieldset//div[1]//input").send_keys("hai")

#relative xpath - copy xpath
driver.find_element(By.XPATH,"//*[@id='pass']").send_keys("1234")

driver.find_element(By.CLASS_NAME,"btn_log").click()


#syntax manual typing - //*[@locator/attribute='value']

driver.find_element(By.XPATH,"//*[@name='user']").send_keys("key")
time.sleep(2)

driver.find_element(By.XPATH,"//*[@type='password']").send_keys("keys")
time.sleep(2)


driver.quit()