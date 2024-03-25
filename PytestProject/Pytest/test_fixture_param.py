from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"],scope='class')
def init__driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.quit()


@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


class Test_Google(BaseTest):

    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"


    def test_google_url(self):
        self.driver.get("http://www.google.com")
        assert self.driver.current_url == "https://www.google.com/"
