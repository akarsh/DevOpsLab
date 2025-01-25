# Experiment 7

# Develop a simple containerized application using Docker

## Dockerfile

Create a file named `Dockerfile` with the following content:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the hello.py script when the container launches
CMD ["python", "hello.py"]
```

## Hello World Python Program

Create a file named `hello.py` with the following content:

```python
print("Hello, World!")
```

## Build the Docker Image

Run the following command to build the Docker image:

```sh
docker build -t hello-world-app .
```

## Run the Docker Container

Run the following command to start a container from the image:

```sh
docker run hello-world-app
```
