# Experiment 12

# Develop test cases for the above containerized application using selenium

## Using Docker Compose for Selenium Firefox to Test HTML, CSS, and JS

1. **Install Docker**: Follow the instructions on the [Docker website](https://docs.docker.com/get-docker/) to install Docker on your machine.

2. **Create Docker Compose File**: Create a `docker-compose.yml` file to set up services for Python and Selenium.

   ```yaml
   services:
     selenium:
       image: selenium/standalone-firefox:latest
       ports:
         - "4444:4444"
       volumes:
         - .:/app
     test:
       image: python:3.8-slim
       volumes:
         - .:/app
       working_dir: /app
       depends_on:
         - selenium
       entrypoint:
         [
           "sh",
           "-c",
           "apt-get update && apt-get install -y netcat-openbsd && while ! nc -z selenium 4444; do sleep 1; done && pip install selenium && python ./test_script_docker.py",
         ]
   ```

3. **Create HTML, CSS, and JS Files**: Create a simple HTML file `index.html` that shows "Hello World" and changes the color via CSS.

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Hello World</title>
       <link rel="stylesheet" href="styles.css" />
     </head>
     <body>
       <h1 id="hello">Hello World</h1>
       <button id="counterButton">Click me</button>
       <p id="counterDisplay">0</p>
       <script src="script.js"></script>
     </body>
   </html>
   ```

4. **Create a CSS File**: Create a CSS file `styles.css` to style the webpage.

   ```css
   body {
     font-family: Arial, sans-serif;
     text-align: center;
     margin-top: 50px;
   }

   #hello {
     color: blue;
   }
   ```

5. **Create a JavaScript File**: Create a JavaScript file `script.js` to add color to the webpage and handle the counter functionality.

   ```javascript
   document.addEventListener("DOMContentLoaded", function () {
     document.getElementById("hello").style.color = "blue";

     let counter = 0;
     const counterButton = document.getElementById("counterButton");
     const counterDisplay = document.getElementById("counterDisplay");

     counterButton.addEventListener("click", function () {
       counter++;
       counterDisplay.textContent = counter;
     });
   });
   ```

6. **Write a Selenium Test Script**: Create a Python script `test_script_docker.py` to test the HTML file.

   ```python
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
   ```

7. **Run the Docker Compose Services**:

   ```sh
   docker compose up --build
   ```

## Explanation of the Test and Output

- The test script uses Selenium to open the local HTML file and check if the content of the element with ID "hello" is "Hello World" and if its color is blue.
- It also tests if the counter increments correctly when the button is clicked.
- If the tests pass, success messages are printed to the console.
- When you run `docker compose up --build`, Docker will build and start the services defined in the `docker-compose.yml` file.
- The `test` service will wait for the `selenium` service to be ready, install the necessary dependencies, and then execute the test script.
- You will see the output of the tests in the Docker console, including the success messages if the tests pass.

## New Features

- Added a button that increments a counter each time it is clicked.
- The counter value is displayed below the button.

## Test Cases

1. Test case to find the HTML element.
2. Test case to update the counter and test it.
