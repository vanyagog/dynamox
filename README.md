# Dynamox Dev-Sec-Fin-Ops Challenge

This project is a submission for the Dynamox Developer Challenge. It contains a backend service for counting successful API requests, deployed in multiple environments.

## 📦 Structure

- `backend/`: FastAPI backend to count successful requests.
- `k8s/`: Kubernetes manifests for Minikube deployment.
- `dev-sec-fin-ops-challenge-answer-template.md`: Challenge answers.

## 🚀 How to run

### Locally

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

Docker
docker build -t backend-counter backend/
docker run -p 8000:8000 backend-counter

Minikube
eval $(minikube docker-env)
docker build -t backend-counter backend/
kubectl apply -f k8s/
minikube service backend

✅ API Endpoints
GET / — test endpoint

GET /count — returns number of successful requests (2xx)
