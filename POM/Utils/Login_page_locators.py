from selenium.webdriver.common.by import By


class LoginPageLocators:

    USERNAME = (By.ID, "user")
    PASSWORD = (By.NAME, "pass")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn_log")