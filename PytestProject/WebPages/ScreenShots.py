# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# driver=webdriver.Firefox()
#
# driver.get("https://www.reddit.com/")
#
# # driver.get_screenshot_as_file("redit.png")
#
# S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
# driver.set_window_size(S('Width'), S('Height'))
# driver.find_element_by_tag_name('body').screenshot('reddit_full_1.png')

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox()
driver.get("https://www.reddit.com/")

# Retrieve the scroll dimensions
scroll_width = driver.execute_script("return Math.max(document.body.scrollWidth, document.documentElement.scrollWidth);")
scroll_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);")

# Set the window size to the entire page
driver.set_window_size(scroll_width, scroll_height)

# Take a screenshot of the entire page
driver.save_screenshot('reddit_full_1.png')

# Close the browser
driver.quit()
