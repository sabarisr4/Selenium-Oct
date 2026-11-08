from selenium import webdriver
import time

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.mycontactform.com")

time.sleep(3)


"""
css - cascade style sheet
manual - 7 ways
short cut :copy=> copy selector


"""

#1.tag name and id      syntax - tag name#id

driver.find_element(By.CSS_SELECTOR, "input#user").send_keys("hello")

#2.tag name and class name     syntax- tag name.class name

driver.find_element(By.CSS_SELECTOR, "input.txt_log").send_keys("hai")

#3.tag name and attribute     syntax - tag name[attribute='value']  #attribute mean without locators called

driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("hai")

#4.tag name and prefix attribute      syntax -tag name[attribute^='pre fix value']
driver.find_element(By.CSS_SELECTOR, "input[type^='te']").send_keys("welcome")

#5.tag name and sur fix attribute      syntax -tag name[attribute$='sur fix value']
driver.find_element(By.CSS_SELECTOR, "input[type$='xt']").send_keys("event")

#6.tag name and substring attribute      syntax -tag name[attribute*='substring value']
driver.find_element(By.CSS_SELECTOR, "input[type*='ex']").send_keys("match")


#7.tag name class name and attribute     syntax -tag name.class name[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input.txt_log[type='text']").send_keys("matching")

#copy selector - right click copy the copy selector

driver.find_element(By.CSS_SELECTOR, "#user").send_keys("mobile")

time.sleep(3)
driver.quit()