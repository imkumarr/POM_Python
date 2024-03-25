from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

# Navigate to the web page
driver.get("http://www.isiri.co/hrm/")

# Define the username input element
username_input = driver.find_element(By.ID, "txtUsername")

# Clear any pre-filled value (optional)
username_input.clear()

# Enter value into the username field
username_input.send_keys("your_username")

# Define the wait
wait = WebDriverWait(driver, 10)

# Use explicit wait for the password field to be clickable
password_input = wait.until(EC.element_to_be_clickable((By.ID, "txtPassword")))

# Perform login by entering the password
password_input.send_keys("your_password")

# Define the login button element
login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginButtonId")))

# Perform login by clicking the login button
login_button.click()

# Continue with other actions after login

# Close the browser
driver.quit()
