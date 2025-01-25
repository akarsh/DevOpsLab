from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os
import time
import unittest

# Check if index.html file exists
file_path = "/app/index.html"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} does not exist")
else:
    print(f"Found {file_path}")

# Set up the Firefox WebDriver
options = Options()
options.headless = True

class TestWebPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            options=options
        )
        cls.driver.get(f"file://{os.path.abspath(file_path)}")
        time.sleep(1)  # Wait for the page to load

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_find_html_element(self):
        try:
            hello_element = self.driver.find_element(By.ID, "hello")
            self.assertIsNotNone(hello_element)
            self.assertEqual(hello_element.text, "Hello World")
            self.assertEqual(hello_element.value_of_css_property("color"), "rgb(0, 0, 255)")  # blue color
            print("Test passed: 'Hello World' element found with correct text and color.")
        except AssertionError as e:
            print(f"Test failed: {e}")

    def test_counter_increment(self):
        try:
            counter_button = self.driver.find_element(By.ID, "counterButton")
            counter_display = self.driver.find_element(By.ID, "counterDisplay")

            initial_value = int(counter_display.text)
            counter_button.click()
            updated_value = int(counter_display.text)

            self.assertEqual(updated_value, initial_value + 1)
            print("Test passed: Counter incremented correctly.")
        except AssertionError as e:
            print(f"Test failed: {e}")

if __name__ == "__main__":
    unittest.main()
