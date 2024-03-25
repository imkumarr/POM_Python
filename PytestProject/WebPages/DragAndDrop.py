import webdriver_manager
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

source=driver.find_element(By.ID, "draggable")
target=driver.find_element(By.ID, "droppable")

act_chains=ActionChains(driver)
act_chains.drag_and_drop(source,target).perform()

driver.quit()

