# Experiment 8

# Integrate Kubernetes and Docker.

## Kubernetes and Docker Integration

Kubernetes and Docker are two essential tools in the world of containerization and orchestration. While Docker is a platform for developing, shipping, and running applications inside containers, Kubernetes is an orchestration system for managing containerized applications at scale.

### Integration

- **Docker**: Docker allows you to package your application and its dependencies into a container, ensuring that it runs consistently across different environments.
- **Kubernetes**: Kubernetes manages these containers, providing features like automated deployment, scaling, and management of containerized applications.

By integrating Docker with Kubernetes, you can leverage the strengths of both tools to build, deploy, and manage scalable applications efficiently.

### Differences

- **Scope**:

  - Docker focuses on the creation and management of individual containers.
  - Kubernetes focuses on the orchestration of multiple containers across a cluster of machines.

- **Components**:

  - Docker includes components like Docker Engine, Docker Compose, and Docker Swarm.
  - Kubernetes includes components like kubectl, kubelet, and kube-scheduler.

- **Scaling**:
  - Docker Swarm provides basic container orchestration and scaling.
  - Kubernetes offers advanced orchestration, scaling, and management capabilities.

Understanding these differences and how they complement each other is crucial for effectively using both tools in your DevOps workflow.

## Steps to Integrate Kubernetes and Docker

1. **Install Docker**:

   - Follow the official Docker installation guide for your operating system: [Docker Installation](https://docs.docker.com/get-docker/)

2. **Install Kubernetes (kubectl and minikube)**:

   - Follow the official Kubernetes installation guide: [Kubernetes Installation](https://kubernetes.io/docs/tasks/tools/)

3. **Start Minikube**:

   ```sh
   minikube start
   ```

4. **Build a Docker Image**:

   - Create a Dockerfile for your application.
   - Build the Docker image:

   ```sh
   docker build -t your-image-name .
   ```

5. **Push Docker Image to a Registry**:

   - Tag your Docker image:

   ```sh
   docker tag your-image-name your-dockerhub-username/your-image-name
   ```

   - Push the image to Docker Hub:

   ```sh
   docker push your-dockerhub-username/your-image-name
   ```

6. **Create a Kubernetes Deployment**:

   - Create a deployment YAML file (e.g., `deployment.yaml`):

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: your-deployment-name
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: your-app-name
     template:
       metadata:
         labels:
           app: your-app-name
       spec:
         containers:
           - name: your-container-name
             image: your-dockerhub-username/your-image-name
             ports:
               - containerPort: 80
   ```

   - Apply the deployment:

   ```sh
   kubectl apply -f deployment.yaml
   ```

7. **Expose the Deployment**:

   - Create a service YAML file (e.g., `service.yaml`):

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: your-service-name
   spec:
     type: LoadBalancer
     selector:
       app: your-app-name
     ports:
       - protocol: TCP
         port: 80
         targetPort: 80
   ```

   - Apply the service:

   ```sh
   kubectl apply -f service.yaml
   ```

8. **Access Your Application**:
   - Get the URL of your application:
   ```sh
   minikube service your-service-name --url
   ```
   - Open the URL in your browser to access your application.
