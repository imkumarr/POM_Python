from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

right_click=driver.find_element(By.XPATH, "//span[text()='right click me']")

act_chains=ActionChains(driver)
act_chains.context_click(right_click).perform()

right_click_1=driver.find_elements(By.CSS_SELECTOR,"li.context-menu-icon span")
for ele in right_click_1:
    print(ele.text)
    if ele.text=='Copy':
        ele.click()
        break
