import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.isiri.co/hrm/")


driver.find_element(By.ID, "txtUsername").send_keys("kumar")
driver.find_element(By.ID, "txtPassword").send_keys("iSiriTech!23")

driver.find_element(By.ID, "btnLogin").click()

driver.find_element(By.ID, "menu_pim_viewPimModule").click()
driver.find_element(By.ID,"empsearch_id").clear()
driver.find_element(By.ID,"empsearch_id").send_keys("007")
driver.find_element(By.NAME,"_search").click()
driver.find_element(By.XPATH, "//a[contains(text(),'007')]").click()
driver.find_element(By.ID,"btnSave").click()

# def drop_down(element, value):
#     dropdown = Select(element)
#     dropdown.select_by_visible_text(value)
#

#
# marital=driver.find_element(By.ID, "personal_cmbMarital")
# country=driver.find_element(By.ID, "personal_cmbNation")
# drop_down(marital, 'Married')
# drop_down(country, "Indian")
# drop_down("personal_cmbNation",'Indian')

# ele=driver.find_element(By.ID, "personal_cmbMarital")
# sel=Select(ele)
# # sel.select_by_visible_text("Single")
# # sel.select_by_value("Single")
# sel.select_by_index(3)


def select_dropdown(options, value):
    for ele in options:
        if ele.text==value:
            ele.click()
            break
mar_opt=driver.find_elements(By.XPATH, "//select[@id='personal_cmbMarital']/option")
select_dropdown(mar_opt,'Single')

time.sleep(8)
driver.quit()