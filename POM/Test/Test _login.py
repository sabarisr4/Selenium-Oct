
from selenium import webdriver


from Pages.Login_page import LoginPage
#from package name .file name import class name

def test_login():



    driver = webdriver.Chrome()

    driver.get("https://www.mycontactform.com")


    login_page = LoginPage(driver) # action name = file name

    login_page.login("Dhivyakarthi123", "12345") # action name.testing name

    driver.quit()


if __name__ == "__main__":
    test_login()