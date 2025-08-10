
# DevOps Analysis

## Processo de lançamento de nova versão dos serviços

1. **Desenvolvimento e commits**  
   O desenvolvedor faz alterações no código e realiza push para o branch principal do repositório (por exemplo, main).

2. **Integração Contínua (CI)**  
   A cada push, é executado o pipeline de CI que realiza: 
   - Verificação da qualidade do código (linters, testes).  
   - Build das imagens Docker para os serviços backend e extractor. 
   - Verificação do sucesso da build.

3. **Deploy Contínuo  (CD)**  
   Após o CI ser bem-sucedido, é executado o processo de CD que inclui:  
   - Tagueamento e publicação das imagens Docker no registro (Docker Hub, GitHub Container Registry ou privado).
   - Atualização dos manifests do Kubernetes com as novas tags das imagens. 
   - Deploy no ambiente de teste/staging. 
   - Testes automáticos ou manuais.

4. **Release em produção**  
   Após testes bem-sucedidos, as atualizações são promovidas para produção, com monitoramento e alertas sobre o status.

## Automação: Pipeline de CI/CD

Para automatizar o processo, propõe-se usar GitHub Actions com o seguinte pipeline:

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

### Comentários

- O acesso ao Docker Registry e Kubernetes é armazenado em variáveis de ambiente e secrets.  
- As imagens são marcadas com a tag do commit para facilitar o rastreamento.
- Os manifests do Kubernetes podem ser parametrizados para usar essas tags, por exemplo, com Helm ou Kustomize.

## Recomendações para melhoria

- Adicionar testes automáticos no pipeline (unitários, integrados).  
- Usar deploys Canary ou Blue-Green para minimizar riscos. 
- Configurar monitoramento e alertas (Prometheus, Grafana, Slack). 
- Implementar confirmação manual do release em produção, se necessário.
---
