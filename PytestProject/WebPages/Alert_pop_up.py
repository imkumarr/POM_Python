
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.find_element(By.NAME, "proceed").click()

alert=driver.switch_to.alert
print(alert)
alert.accept()

driver.switch_to.default_content()