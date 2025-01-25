# Experiment 5

# Demonstrate continuous integration and development using Jenkins.

## Prerequisites

- Docker installed
- Git installed
- A GitHub repository

## Setup Jenkins with Docker

1. Build the Docker image:

   ```sh
   docker build -t jenkins-docker . --platform=linux/amd64
   ```

2. Run the Docker container:

   ```sh
   docker run -d -p 8080:8080 -p 50000:50000 --name jenkins-docker jenkins-docker
   ```

3. Access Jenkins at `http://localhost:8080` and complete the setup process.

## Steps

1. **Create a Jenkins Pipeline:**

   - Open Jenkins and create a new pipeline job.
   - In the pipeline configuration, define your pipeline script.

2. **Configure Source Code Management:**

   - Under the Source Code Management section, select Git.
   - Enter the repository URL and credentials if required.

3. **Define Build Steps:**

   - In the pipeline script, define the stages for building, testing, and deploying your application.

4. **Run the Pipeline:**

   - Save the configuration and run the pipeline.
   - Monitor the build process and ensure it completes successfully.

5. **Continuous Integration:**

   - Make changes to your code and push them to the repository.
   - Observe Jenkins automatically triggering the pipeline and running the build.

6. **Continuous Deployment:**
   - Configure the pipeline to deploy the application to a server or cloud service after a successful build.

## Example: Using Jenkins to create a pipeline job

### Prerequisites

- Jenkins installed and running

### Setup

1. Open Jenkins and create a new pipeline job named `Hello World Pipeline`.
2. Add the below pipeline script

### Jenkins Pipeline Script

```groovy
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
```

### Running the Pipeline

1. Save the pipeline configuration.
2. Run the pipeline and monitor the build process.
3. Make changes to the Experiment1 files and push them to the repository.
4. Observe Jenkins automatically triggering the pipeline and running the build and test stages.

## Conclusion

By following these steps, you have demonstrated continuous integration and development using Jenkins.
