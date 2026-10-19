# Flask on Minikube

A small Flask application packaged with Gunicorn and deployed to Kubernetes on Minikube.

## Prerequisites

- Docker
- Minikube
- kubectl
- Python 3.12+ (only needed to run the tests outside Docker)

## Build and deploy (PowerShell)

Run these commands from the `flask-minikube` directory:

```powershell
minikube start
docker build -t flask-minikube:local .
minikube image load flask-minikube:local
kubectl apply -f .\k8s\
kubectl rollout status deployment/flask-app
kubectl get pods,services
```

The Deployment uses `imagePullPolicy: Never`, so Minikube runs the locally loaded image rather than trying to pull it from a registry.

## Open the application

Forward the Kubernetes Service to localhost:

```powershell
kubectl port-forward service/flask-app 8080:80
```

While port-forwarding is running, open `http://127.0.0.1:8080/` or check the health endpoint at `http://127.0.0.1:8080/health`. Stop port-forwarding with Ctrl+C.

Alternatively, use `minikube service flask-app --url`.

## Run tests locally

```powershell
python -m pip install -r requirements.txt
python -m unittest discover -s tests
```

## Update the application

After changing the code, rebuild and reload the image, then restart the Deployment:

```powershell
docker build -t flask-minikube:local .
minikube image load flask-minikube:local
kubectl rollout restart deployment/flask-app
kubectl rollout status deployment/flask-app
```
