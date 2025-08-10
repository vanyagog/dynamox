# Dynamox Dev-Sec-Fin-Ops Challenge

## Descrição do projeto

Esta é a implementação da tarefa de teste para o Dynamox Dev-Sec-Fin-Ops Challenge.
O projeto inclui dois componentes:

- **Backend Deployment** — um serviço em FastAPI que conta a quantidade de requisições API bem-sucedidas.  
- **Extraction CronJob** — um serviço que a cada 15 minutos extrai a quantidade atual de requisições bem-sucedidas do Backend.

Ambos os serviços podem ser executados localmente, no Docker e no Kubernetes (Minikube).

---

## Estrutura do projeto
```
dev-sec-fin-ops-challenge/
│
├── backend/ # Backend Deployment
│ ├── main.py
│ ├── requirements.txt
│ ├── Dockerfile
│ └── README.md
│
├── extractor/ # Extraction CronJob
│ ├── extractor.py
│ ├── requirements.txt
│ ├── Dockerfile
│ └── README.md
│
├── k8s/ # Kubernetes манифесты
│ ├── backend-deployment.yaml
│ ├── backend-service.yaml
│ └── extractor-cronjob.yaml
│
├── dev-sec-fin-ops-challenge-answer-template.md # Технический отчёт
├── .gitignore
└── README.md 
```
---

## Componentes e execução

### Backend Deployment

Serviço em FastAPI que:

- conta o número de requisições HTTP bem-sucedidas (status 2xx),
- disponibiliza uma API REST /count com esse número.

#### Execução local
```
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
Сервис будет доступен по адресу:
http://127.0.0.1:8000/
```

Verificação da API:
```
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/count
```

Execução no Docker:
```
docker build -t backend-counter backend/
docker run -p 8000:8000 backend-counter
```

Execução no Minikube
```
eval $(minikube docker-env)
docker build -t backend-counter backend/
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
minikube service backend
```

Extraction CronJob
Serviço que a cada 15 minutos solicita o número de requisições bem-sucedidas do Backend e registra o resultado no log.

Execução local
```
cd extractor
pip install -r requirements.txt
BACKEND_URL=http://127.0.0.1:8000/count python extractor.py
```

Execução no Docker
```
docker build -t extractor extractor/
docker run --rm -e BACKEND_URL="http://backend:8000/count" extractor
```

Execução no Minikube (Kubernetes CronJob)
```
eval $(minikube docker-env)
docker build -t extractor extractor/
kubectl apply -f k8s/extractor-cronjob.yaml
kubectl get cronjobs
kubectl get jobs
kubectl logs <job-pod-name>
```

Variáveis de ambiente

| Variável        | Descrição                                  | Valor padrão                      |
|-----------------|--------------------------------------------|-----------------------------------|
| BACKEND_URL     | URL para consulta do número de requisições bem-sucedidas | http://127.0.0.1:8000/count (localmente) |

