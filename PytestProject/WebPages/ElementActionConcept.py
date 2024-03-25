from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("http://www.isiri.co/hrm/")

user_name=driver.find_element(By.CSS_SELECTOR, "#txtUsername")
Pass_word=driver.find_element(By.CSS_SELECTOR, "#txtPassword")
Login=driver.find_element(By.XPATH, "//input[@id='btnLogin' and @class='button']")

act_chains=ActionChains(driver)
act_chains.send_keys_to_element(user_name,"kumar")
act_chains.send_keys_to_element(Pass_word, "iSiriTech!23")
act_chains.click(Login).perform()