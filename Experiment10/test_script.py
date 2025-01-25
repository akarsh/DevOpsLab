from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Set up the Firefox WebDriver
options = Options()
options.headless = True
driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    options=options
)

# Test: Open Selenium website and check the page title
driver.get("https://www.selenium.dev")
assert "Selenium" in driver.title

# Print success message
print("Test passed: Selenium website title is correct.")

driver.quit()
