from Utils.Login_page_locators import LoginPageLocators

#from package name .file name import class name

class LoginPage:

    def __init__(self, driver): # stores the Selenium browser driver inside the LoginPage
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def login(self, username, password): # for order purpose
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()