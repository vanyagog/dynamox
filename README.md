# Dynamox Dev-Sec-Fin-Ops Challenge

## Описание проекта

Это реализация тестового задания для Dynamox Dev-Sec-Fin-Ops Challenge.  
Проект включает два компонента:

- **Backend Deployment** — сервис на FastAPI, считающий количество успешных API-запросов.  
- **Extraction CronJob** — сервис, который каждые 15 минут извлекает текущее количество успешных запросов из Backend.

Оба сервиса можно запускать локально, в Docker и в Kubernetes (Minikube).

---

## Структура проекта

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
└── README.md # Этот файл

yaml
Копировать
Редактировать

---

## Компоненты и запуск

### Backend Deployment

Сервис на FastAPI, который:

- считает количество успешных HTTP-запросов (статус 2xx),
- предоставляет REST API `/count` с этим числом.

#### Запуск локально

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
Сервис будет доступен по адресу:
http://127.0.0.1:8000/

Проверка API:

bash
Копировать
Редактировать
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/count
Запуск в Docker
bash
Копировать
Редактировать
docker build -t backend-counter backend/
docker run -p 8000:8000 backend-counter
Запуск в Minikube
bash
Копировать
Редактировать
eval $(minikube docker-env)
docker build -t backend-counter backend/
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
minikube service backend
Extraction CronJob
Сервис, который каждые 15 минут запрашивает количество успешных запросов из Backend и выводит результат в лог.

Запуск локально
bash
Копировать
Редактировать
cd extractor
pip install -r requirements.txt
BACKEND_URL=http://127.0.0.1:8000/count python extractor.py
Запуск в Docker
bash
Копировать
Редактировать
docker build -t extractor extractor/
docker run --rm -e BACKEND_URL="http://backend:8000/count" extractor
Запуск в Minikube (Kubernetes CronJob)
bash
Копировать
Редактировать
eval $(minikube docker-env)
docker build -t extractor extractor/
kubectl apply -f k8s/extractor-cronjob.yaml
kubectl get cronjobs
kubectl get jobs
kubectl logs <job-pod-name>
Переменные окружения
Переменная	Описание	Значение по умолчанию
BACKEND_URL	URL для запроса количества успешных запросов	http://127.0.0.1:8000/count (локально)
