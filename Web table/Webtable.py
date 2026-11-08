from selenium import webdriver
import time

from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice/")

time.sleep(3)

"""
copy the xpath for common of two rows
copy the xpath for common of two columns

copy the xpath of particular columns
"""


#copy the xpath for common of two rows
rows=driver.find_elements(By.XPATH,"//*[@id='product']//tbody//tr")
print("num of rows",len(rows))

#copy the xpath for common of two columns
cols=driver.find_elements(By.XPATH,"//*[@id='product']//tbody//tr[1]//th")
print("num of columns",len(cols))

#copy the xpath of particular columns
data=driver.find_element(By.XPATH,"//*[@id='product']//tbody//tr[3]//td[3]").text
print(data)

#For list view
for i in range(1,4):
    data1=driver.find_elements(By.XPATH,"//*[@id='product']//tbody//tr[2]//td["+str(i)+"]")
    for i in data1:
         print(i.text)