from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage=LoginPage(self.driver)
        homePage=self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        title=homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginPage=LoginPage(self.driver)
        homePage=self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        header=homePage.get_header_value()
        assert  header== TestData.HOME_PAGE_HEADER

    def test_home_page_account_name(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        account_name = homePage.get_header_value()
        assert account_name == TestData.ACCOUNT_NAME

    def test_setting_icon(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.is_setting_icon_exist()