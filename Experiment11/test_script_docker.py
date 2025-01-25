from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os
import time  # Added import for time

# Check if index.html file exists
file_path = "/app/index.html"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} does not exist")
else:
    print(f"Found {file_path}")

# Set up the Firefox WebDriver
options = Options()
options.headless = True
driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    options=options
)

# Wait for the Selenium server to be ready
time.sleep(1)

try:
    # Test: Open the local HTML file and check the content and color
    abs_file_path = os.path.abspath(file_path)
    print(f"Absolute file path: {abs_file_path}")
    driver.get(f"file://{abs_file_path}")
    element = driver.find_element(By.ID, "hello")
    assert element.text == "Hello World"
    assert element.value_of_css_property("color") == "rgb(0, 0, 255)"  # blue color

    # Print success message
    print("Test passed: 'Hello World' is displayed correctly with blue color.")
finally:
    driver.quit()  # Ensure the WebDriver quits even if an assertion fails
