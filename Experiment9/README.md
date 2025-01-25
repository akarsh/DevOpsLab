# Experiment 9

# Automate the process of running containerized application developed in experiment 7 using kubernetes

## Introduction
In this experiment, we will automate the deployment of a containerized application using Kubernetes. This involves creating Kubernetes manifests for the application and deploying it to a Kubernetes cluster.

## Prerequisites
- Docker installed
- Minikube installed and running
- kubectl installed and configured
- Ensure you have the necessary permissions to create resources in the Kubernetes cluster

## Steps

### 1. Start Minikube
Start Minikube to create a local Kubernetes cluster:
```sh
minikube start
```

### 2. Set Minikube Context
Set Minikube as the Kubernetes context:
```sh
kubectl config use-context minikube
```

### 3. Create and Expose Deployment
Create a sample deployment and expose it on port 8080:
```sh
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube --type=NodePort --port=8080
```

It may take a moment, but your deployment will soon show up when you run:
```sh
kubectl get services hello-minikube
```

The easiest way to access this service is to let Minikube launch a web browser for you:
```sh
minikube service hello-minikube
```

### 4. Check Minikube Dashboard
You can also check the Minikube dashboard to monitor your cluster:
```sh
minikube dashboard
```

## Conclusion
By following these steps, you have automated the deployment of a containerized application using Kubernetes with Minikube.
