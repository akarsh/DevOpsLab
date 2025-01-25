# Experiment 6

# Explore Docker commands for content management.

## Introduction

In this experiment, we will explore various Docker commands used for content management. Docker is a platform that enables developers to automate the deployment of applications inside lightweight, portable containers.

## Objectives

- Understand the basic Docker commands for managing content.
- Learn how to create, manage, and delete Docker images and containers.
- Explore Docker volumes and networks.

## Docker Commands for Content Management

1. **docker pull**: Download an image from a Docker registry.

   ```sh
   docker pull <image_name>
   ```

2. **docker images**: List all Docker images on the local machine.

   ```sh
   docker images
   ```

3. **docker rmi**: Remove one or more Docker images.

   ```sh
   docker rmi <image_name>
   ```

4. **docker run**: Create and start a new container from an image.

   ```sh
   docker run <image_name>
   ```

5. **docker ps**: List all running containers.

   ```sh
   docker ps
   ```

6. **docker stop**: Stop a running container.

   ```sh
   docker stop <container_id>
   ```

7. **docker rm**: Remove one or more stopped containers.

   ```sh
   docker rm <container_id>
   ```

8. **docker volume**: Manage Docker volumes.

   ```sh
   docker volume ls
   docker volume create <volume_name>
   docker volume rm <volume_name>
   ```

9. **docker network**: Manage Docker networks.
   ```sh
   docker network ls
   docker network create <network_name>
   docker network rm <network_name>
   ```

## Example: Running a Nginx Container

Let's run an example to demonstrate the usage of Docker commands by running an Nginx container.

1. **Pull the Nginx image**:

   ```sh
   docker pull nginx
   ```

2. **Run the Nginx container**:

   ```sh
   docker run --name mynginx -d -p 8080:80 nginx
   ```

   This command will start an Nginx container named `mynginx` and map port 8080 on the host to port 80 in the container.

3. **List running containers**:

   ```sh
   docker ps
   ```

4. **Explore Nginx in the browser**:
   Open your web browser and navigate to `http://localhost:8080`. You should see the Nginx welcome page.

5. **Stop the Nginx container**:

   ```sh
   docker stop mynginx
   ```

6. **Remove the Nginx container**:

   ```sh
   docker rm mynginx
   ```

7. **Remove the Nginx image**:
   ```sh
   docker rmi nginx
   ```
