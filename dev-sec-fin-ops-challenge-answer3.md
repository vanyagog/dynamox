
# DevOps Analysis

## Процесс выпуска новой версии сервисов

1. **Разработка и коммиты**  
   Разработчик вносит изменения в код и пушит их в основную ветку репозитория (например, `main`).

2. **Continuous Integration (CI)**  
   При каждом пуше запускается CI-пайплайн, который выполняет:  
   - Проверку качества кода (линтеры, тесты).  
   - Сборку Docker-образов для backend и extractor сервисов.  
   - Проверку успешности сборки.

3. **Continuous Deployment (CD)**  
   После успешного CI выполняется CD-процесс, включающий:  
   - Тэгирование и публикацию Docker-образов в реестр (Docker Hub, GitHub Container Registry или приватный).  
   - Обновление Kubernetes-манифестов с новыми тегами образов.  
   - Деплой в тестовое/staging окружение.  
   - Автоматическое или ручное тестирование.

4. **Релиз в production**  
   После успешного тестирования обновления продвигаются в production, с мониторингом и оповещениями о статусе.

## Автоматизация: CI/CD Pipeline

Для автоматизации процесса предлагается использовать GitHub Actions с таким пайплайном:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    env:
      DOCKER_REGISTRY: ghcr.io
      IMAGE_BACKEND: ${{ env.DOCKER_REGISTRY }}/your-org/backend-counter
      IMAGE_EXTRACTOR: ${{ env.DOCKER_REGISTRY }}/your-org/extractor
    steps:
      - uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Login to Docker Registry
        uses: docker/login-action@v2
        with:
          registry: ${{ env.DOCKER_REGISTRY }}
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push backend image
        working-directory: ./backend
        run: |
          docker build -t $IMAGE_BACKEND:${{ github.sha }} .
          docker push $IMAGE_BACKEND:${{ github.sha }}

      - name: Build and push extractor image
        working-directory: ./extractor
        run: |
          docker build -t $IMAGE_EXTRACTOR:${{ github.sha }} .
          docker push $IMAGE_EXTRACTOR:${{ github.sha }}

      - name: Deploy to Kubernetes
        uses: appleboy/kubectl-action@v0.1.9
        with:
          kubeconfig: ${{ secrets.KUBE_CONFIG }}
          args: apply -f k8s/
```

### Комментарии

- В переменных окружения и секретах хранится доступ к Docker Registry и Kubernetes.  
- Образы помечаются тегом коммита для удобства отслеживания.  
- Манифесты Kubernetes можно параметризовать для использования этих тегов, например с помощью Helm или Kustomize.

## Рекомендации по улучшению

- Добавить автоматическое тестирование в пайплайн (юнит, интеграционные тесты).  
- Использовать Canary или Blue-Green деплойменты для минимизации рисков.  
- Настроить мониторинг и алертинг (Prometheus, Grafana, Slack).  
- Организовать ручное подтверждение релиза в production, если требуется.

---
