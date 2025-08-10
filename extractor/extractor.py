import requests
import datetime

BACKEND_URL = "http://backend:8000/count"  # для Minikube/Docker
# Для локального теста можно заменить на:
# BACKEND_URL = "http://localhost:8000/count"

def extract():
    try:
        response = requests.get(BACKEND_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"[{datetime.datetime.now()}] Successful requests: {data['successful_requests']}")
        else:
            print(f"[{datetime.datetime.now()}] Error: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] Exception: {e}")

if __name__ == "__main__":
    extract()
