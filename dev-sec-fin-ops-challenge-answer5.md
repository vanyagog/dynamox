
# FinOps Analysis

## Avaliação do custo dos serviços no Google Cloud

### Dados de entrada

| Atributo        | Backend Deployment       | Extraction Cronjob         |
|----------------|-------------------------|----------------------------|
| Machine Type   | n1-highcpu-4            | n1-highmem-2               |
| Number of Pods | 55                      | 28                         |
| CPU            | 1.25                    | 0.5                        |
| Memory         | 512 Mi (0.5 Gi)         | 2 Gi                       |

### Preços aproximados (estimativa)

| Máquina          | Preço por hora (USD)         |
|----------------|--------------------------|
| n1-highcpu-4   | 0.60                     |
| n1-highmem-2   | 0.38                     |

---

### Cálculo do Backend Deployment

- CPU total para todos os pods: 55 × 1,25 = 68,75 CPUs 
- Memória: 55 × 0,5 Gi = 27,5 Gi
- A máquina n1-highcpu-4 possui 4 CPUs e 3,6 Gi de memória 
- São necessárias pelo menos 18 máquinas deste tipo (baseado em CPU)
- Custo por hora: 18 × 0,60 = 10,8 USD
- Custo por dia: 10,8 × 24 = 259,2 USD
- Custo por 30 dias: 259,2 × 30 = 7.776 USD
- Custo por 365 dias: 259,2 × 365 = 94.608 USD  

### Cálculo do Extraction Cronjob

- CPU total para todos os pods: 28 × 0.5 = 14 CPU  
- Memória: 28 × 2 Gi = 56 Gi  
- A máquina n1-highcpu-2 possui 2 CPU e 13 Gi de memória   
- São necessárias pelo menos 7 máquinas deste tipo (baseado em CPU)  
- Custo por hora: 7 × 0.38 = 2.66 USD  
- Custo por dia: 2.66 × 24 = 63.84 USD  
- Custo por 30 dias: 63.84 × 30 = 1,915.2 USD  
- Custo por 365 dias: 63.84 × 365 = 23,301.6 USD  

---

### Avaliação final dos custos

| Serviço              | 30 dias (USD) | 365 dias (USD) |
|--------------------|---------------|----------------|
| Backend Deployment  | 7,776         | 94,608         |
| Extraction Cronjob  | 1,915.2       | 23,301.6       |
| **Total**          | **9,691.2**   | **117,909.6**  |

---

### Recomendações para otimização de custos

- Executar ambientes de teste com menor quantidade de pods.  
- Utilizar instâncias preemptíveis (spot instances).  
- Escalar automaticamente a carga usando HPA (Horizontal Pod Autoscaler).
- Otimizar o uso de CPU e memória.
- Considerar tipos de máquinas e regiões alternativas.

---
