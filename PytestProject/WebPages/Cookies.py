from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
# print(driver.get_cookies())

driver.add_cookie({"name":"kumar","domain":"reddit.com","value":"python"})
# print(driver.get_cookies())

cookies=driver.get_cookies()

for ele in cookies:
    print(cookies)