# Experiment 10

# Install and explore selenium for automated testing

## Using Python, Selenium, and Docker for Testing

1. **Install Docker**: Follow the instructions on the [Docker website](https://docs.docker.com/get-docker/) to install Docker on your machine.

2. **Create Docker Compose File**: Create a `docker-compose.yml` file to set up services for Python and Selenium.

   ```yaml
   version: "3"
   services:
     selenium:
       image: selenium/standalone-firefox:latest
       ports:
         - "4444:4444"
     test:
       image: python:3.8-slim
       volumes:
         - .:/app
       working_dir: /app
       depends_on:
         - selenium
       entrypoint: ["sh", "-c", "apt-get update && apt-get install -y netcat-openbsd && while ! nc -z selenium 4444; do sleep 1; done && pip install selenium && python ./test_script.py"]
   ```

3. **Write a Selenium Test Script**: Create a Python script `test_script.py` with Selenium tests.

   ```python
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
   ```

4. **Run the Docker Compose Services**:

   ```sh
   docker compose up --build
   ```

## Explanation of the Test and Output

- The test script uses Selenium to open the Selenium website and check if the page title contains the word "Selenium".
- If the test passes, a success message "Test passed: Selenium website title is correct." is printed to the console.
- When you run `docker compose up --build`, Docker will build and start the services defined in the `docker-compose.yml` file.
- The `test` service will wait for the `selenium` service to be ready, install the necessary dependencies, and then execute the test script.
- You will see the output of the test in the Docker console, including the success message if the test passes.
