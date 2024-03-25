from selenium.webdriver.common.by import By
from selenium import webdriver
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.ID, "btnLogin")
    SIGNUP_LINK = (By.LINK_TEXT, "Forgot your password?")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self,title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)
