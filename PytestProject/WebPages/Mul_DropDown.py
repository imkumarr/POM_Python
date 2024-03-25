import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")


def drop_down(option, value):
    for ele in option:
        print(ele.text)
        for k in range(len(value)):
            if ele.text==value[k]:
                ele.click()
                break

driver.find_element(By.ID, "justAnInputBox").click()
mul_dropdown=driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
value_list=['choice 2','choice 6']
drop_down(mul_dropdown,value_list)
#//li[@class='ComboTreeItemChlid']/span
time.sleep(8)
driver.quit()


