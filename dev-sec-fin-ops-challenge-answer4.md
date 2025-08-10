
# SecOps Analysis

## Riscos potenciais de segurança

| Risco                                         | Descrição                                                                                  |
|----------------------------------------------|-------------------------------------------------------------------------------------------|
| 1. Acesso não autenticado à API        | 	O backend da API está acessível sem autenticação, permitindo que qualquer pessoa obtenha dados e distorça as estatísticas. |
| 2. Falta de criptografia do tráfego            | 	O tráfego entre o cliente e o serviço é transmitido sem HTTPS, podendo levar à interceptação e alteração dos dados. |
| 3. Vulnerabilidades em bibliotecas de terceiros        | As bibliotecas Python utilizadas podem conter vulnerabilidades conhecidas.                      |
| 4. Isolamento insuficiente dos containers        | Os containers podem ter privilégios excessivos e capacidades de interação não controladas.               |
| 5. Armazenamento de segredos e senhas em texto aberto| Segredos e senhas podem ser armazenados incorretamente, aumentando o risco de comprometimento.    |
| 6. Monitoramento e logging insuficientes    | A ausência de logging centralizado e monitoramento dificulta a detecção de incidentes. |
| 7. Possíveis ataques DoS                        | 	A falta de limitação no número de requisições pode levar à sobrecarga do serviço.           |
| 8. Permissões inseguras no Kubernetes   | Permissões excessivas podem levar à escalada de privilégios dentro do cluster.           |

## Medidas para mitigação de riscos

- Implementar autenticação e autorização na API (por exemplo, OAuth2, JWT ou chaves de API).  
- Configurar HTTPS/TLS para todas as comunicações externas e internas (Ingress com certificados Let's Encrypt).  
- Atualizar regularmente as dependências e usar ferramentas de análise de vulnerabilidades (Snyk, Dependabot).
- Configurar políticas de segurança para containers (Pod Security Policies, seccomp, AppArmor).
- Armazenar segredos apenas em Kubernetes Secrets ou em sistemas especializados de gerenciamento de segredos (HashiCorp Vault).
- Implementar logging e monitoramento centralizados com alertas (ELK, Prometheus, Grafana, Alertmanager).
- Aplicar rate limiting e proteção contra DoS no nível do API Gateway ou controlador Ingress.
- Minimizar permissões no Kubernetes usando RBAC e o princípio do menor privilégio.

## Recomendações para implementação

- Usar o suporte nativo a OAuth2/JWT do FastAPI para proteger a API.
- Configurar o controlador Ingress com TLS e autenticação básica.
- Incluir verificação de segurança das dependências no pipeline CI/CD.
- Restringir permissões das contas de serviço Kubernetes usadas pelas aplicações.
- Configurar monitoramento e alertas para atividade suspeita.

---
