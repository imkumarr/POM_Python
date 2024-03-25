from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.isiri.co/hrm/")

element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "textUsernme")))

driver.quit()