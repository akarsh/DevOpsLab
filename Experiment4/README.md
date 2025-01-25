# Experiment 4

# Jenkins installation and setup, explore the environment.

## About Jenkins

Jenkins is an open-source automation server that helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration and continuous delivery (CI/CD).

## How to Install Jenkins

### Using Docker

1. **Install Docker:**
   If Docker is not already installed, follow the instructions on the [Docker website](https://docs.docker.com/get-docker/) to install it.

2. **Run Jenkins Container:**
   Pull the Jenkins image and run it in a container.
   ```sh
   docker pull jenkins/jenkins:lts
   docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
   ```
   - `docker pull jenkins/jenkins:lts`: This command pulls the latest stable (LTS) Jenkins image from the Docker repository.
   - `docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts`: This command runs the Jenkins container with the following options:
     - `-p 8080:8080`: Maps port 8080 on the host to port 8080 on the container, allowing access to the Jenkins web interface.
     - `-p 50000:50000`: Maps port 50000 on the host to port 50000 on the container, used for Jenkins agent communication.
     - `-v jenkins_home:/var/jenkins_home`: Mounts the `jenkins_home` volume to persist Jenkins data.

## How to Start Jenkins

1. **Access Jenkins:**
   Open your web browser and go to `http://localhost:8080`. You will see the Jenkins setup wizard.

## How to Explore Jenkins

1. **Unlock Jenkins:**
   Retrieve the initial admin password.

   ```sh
   docker exec -it <container_id> cat /var/jenkins_home/secrets/initialAdminPassword
   ```

   Enter this password in the setup wizard to unlock Jenkins.

2. **Install Suggested Plugins:**
   Follow the setup wizard to install the suggested plugins.

3. **Create Admin User:**
   Create your first admin user as prompted by the setup wizard.

4. **Start Using Jenkins:**
   Once the setup is complete, you can start creating jobs, configuring pipelines, and exploring Jenkins features.
