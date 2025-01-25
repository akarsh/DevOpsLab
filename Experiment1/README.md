# Experiment 1

# Write code for a simple user registration form for an event.

## Files

- `app.py`: The main Flask application file that contains the routes and logic for the user registration form.
- `Dockerfile`: The Dockerfile used to build the Docker image for the Flask application.
- `Dockerfile.test`: The Dockerfile used to build the Docker image for running unit tests on the Flask application.
- `requirements.txt`: A file listing the Python dependencies required to run the Flask application.
- `templates/`: A directory containing HTML templates for the Flask application.
  - `register.html`: The HTML template for the user registration form.
  - `success.html`: The HTML template displayed after a successful user registration.

## Build

To build the Docker image for the Flask application, run the following command:

```sh
docker build --no-cache -t simple-flask-app .
```

## Run

To run the Docker container for the Flask application, use the following command:

```sh
docker run -p 80:80 simple-flask-app
```

After running the container, open your web browser and navigate to `http://0.0.0.0:80/register` to access the user registration form.

## Testing

To run the unit tests for `app.py` using Docker, follow these steps:

1. Build the Docker image for testing:

```sh
docker build -f Dockerfile.test -t simple-flask-app-test .
```

2. Run the Docker container to execute the tests:

```sh
docker run simple-flask-app-test
```

This command will discover and run all the unit tests in the `test_app.py` file.
