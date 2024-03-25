from telnetlib import EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver):
        self.driver=driver

        def do_click(self,by_locator):
            WebDriverWait(self.driver,10).until(EC.visiblity_of_element(by_locator)).click()


        def do_send_keys(self,by_locator,text):
            WebDriverWait(self.driver,10).until(EC.visiblity_of_element(by_locator)).send_keys(text)

        def get_element(self,by_locator):
           element= WebDriverWait(self.driver,10).until(EC.visiblity_of_element(by_locator))
           return element.text

        def is_enabled(self,by_locator):
           element= WebDriverWait(self.driver,10).until(EC.visiblity_of_element(by_locator))
           return bool(element)


        def get_title(self,title):
            WebDriverWait(self.driver,10).until(EC.title_is(title))
            return self.driver.title








