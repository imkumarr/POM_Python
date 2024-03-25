import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("http://www.isiri.co/hrm/")

driver.find_element(By.LINK_TEXT, "Forgot your password?").click()
driver.back()
time.sleep(8)
driver.forward()
time.sleep(6)
driver.back()
time.sleep(6)
driver.refresh()
