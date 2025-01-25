from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os

# Set up the Firefox WebDriver
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# Test: Open the local HTML file and check the content and color
file_path = "file:///Users/akarshseggemu/Development/01DevOps-Lab/Experiment11/index.html"  # Update this path to the location of your index.html file
driver.get(file_path)
element = driver.find_element(By.ID, "hello")
assert element.text == "Hello World"
assert element.value_of_css_property("color") == "rgb(0, 0, 255)"  # blue color

# Print success message
print("Test passed: 'Hello World' is displayed correctly with blue color.")

driver.quit()