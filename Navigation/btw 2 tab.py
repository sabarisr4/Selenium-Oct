
from selenium import webdriver
import time


from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")

# open mycontactform.com in a new tab
driver.execute_script("window.open('http://www.google.com','_blank');")

time.sleep(3)


# collect control of first tab: driver.current_window_handle => parent_handle
# collecting handles of two tabs => driver.window_handles


handles = driver.window_handles #collect two tabs
size=len(handles) #size
parent_handle=driver.current_window_handle #set parent handle has google


"""
parent_handle=> control of google
handles=>[ google , mycontactform]
First iteration:  x=0
     handles[0] != parent handle:
     google !=google 

second iteration: x=1
     handles[1]!=parent handle
     seleniumeasy.com!=google
         driver.switch_to.window(handles[1])
         switching control to mycontactform.com
         clicking on linktext
         close=> close the mycontactform.com


switching control back to google
getting title of google
clicking on images link text
"""

for x in range(size):  # for x in in range(2):      0,1
     if handles[x]!=parent_handle:
       driver.switch_to.window(handles[x]) #switch to 1 it mean my contactform
       print(driver.title)
       time.sleep(1)
       driver.find_element(By.LINK_TEXT, "Gmail").click()
       time.sleep(3)
       driver.close()  # window which in focus will be close
       # quit=> close all the tabs
       break


driver.switch_to.window(parent_handle)
print(driver.title)
driver.find_element(By.LINK_TEXT,"Images").click()
driver.quit()