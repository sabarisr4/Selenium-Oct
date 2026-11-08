from selenium import webdriver
import time

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.mycontactform.com")

time.sleep(3)


"""

dynamic xpath

following
preceding

parent
child

following - sibling
preceding - sibling

"""


#First find username xpath and then take the tag name of login button and ctrl F and paste and type //following::tag name
driver.find_element(By.XPATH, "//*[@id='user']//following::input[2]").click()
time.sleep(3)

#First find login xpath and then take the tag name of username and ctrl F and paste and type //preceding::tag name
driver.find_element(By.XPATH, "//*[@id='right_col_top']/form/div/input//preceding::input[2]").send_keys("Hai")
time.sleep(3)

#parent to child
print(driver.find_element(By.XPATH,"//*[@id='right_col_bottom']//child::p[2]").text)
time.sleep(3)

#child to parent
print(driver.find_element(By.XPATH,"//*[@id='right_col_bottom']//parent::p[1]").location)
time.sleep(3)

#following  -sibling
print(driver.find_element(By.XPATH,"//*[@id='right_col_bottom']/img//following-sibling::p[3]").text)
time.sleep(3)

#preceding  -sibling
print(driver.find_element(By.XPATH,"//*[@id='right_col_bottom']/img//following-sibling::p[1]").text)
time.sleep(1)


driver.quit()