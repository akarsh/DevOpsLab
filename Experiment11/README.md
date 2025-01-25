# Experiment 11

# Write a simple program in JavaScript and perform testing using Selenium

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

5. **Create a JavaScript File**: Create a JavaScript file `script.js` to add color to the webpage.

   ```javascript
   document.getElementById("hello").style.color = "blue";
   ```

6. **Write a Selenium Test Script**: Create a Python script `test_script_docker.py` to test the HTML file.

   ```python
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
   ```

7. **Run the Docker Compose Services**:

   ```sh
   docker compose up --build
   ```

## Explanation of the Test and Output

- The test script uses Selenium to open the local HTML file and check if the content of the element with ID "hello" is "Hello World" and if its color is blue.
- If the test passes, a success message "Test passed: 'Hello World' is displayed correctly with blue color." is printed to the console.
- When you run `docker compose up --build`, Docker will build and start the services defined in the `docker-compose.yml` file.
- The `test` service will wait for the `selenium` service to be ready, install the necessary dependencies, and then execute the test script.
- You will see the output of the test in the Docker console, including the success message if the test passes.
