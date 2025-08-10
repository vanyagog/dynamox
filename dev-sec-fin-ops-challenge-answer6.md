
# Bonus

## 6.1 Diagrama arquitetônico

<img width="1536" height="1024" alt="ChatGPT Image 10 авг  2025 г , 21_45_00" src="https://github.com/user-attachments/assets/bfde08a0-3b6c-4191-bc4c-01a0d2f5566f" />


## Um exemplo simples de autorização jwt pode ser visto na pasta jwt 

**Por exemplo, uma base de usuários simples na memória é usada (por exemplo)
mas é melhor usar um banco de dados relacional Postgresql** 

```
jwt/
├── main.py
├── auth.py
├── users.py
├── requirements.txt
└── Dockerfile
```

Execução local
```
cd jwt
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Defina o segredo (em produção - em env/k8s Secret):

```
export JWT_SECRET="supersecretvalue"
```

Execução

```
uvicorn main:app --reload
```

Verificação

```
[root@localhost ~]# curl -X POST "http://127.0.0.1:8000/token" -d "username=alice&password=alicepassword"
{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGljZSIsInNjb3BlcyI6WyJyZWFkIl0sImlhdCI6MTc1NDg2MTMxMiwiZXhwIjoxNzU0ODY0OTEyfQ.ilOxNvpZhOf6puHwhYwmdrt3v0XurDqRRNNZrAliErQ","token_type":"bearer"}[root@localhost ~]#
[root@localhost ~]#
[root@localhost ~]# curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGljZSIsInNjb3BlcyI6WyJyZWFkIl0sImlhdCI6MTc1NDg2MTMxMiwiZXhwIjoxNzU0ODY0OTEyfQ.ilOxNvpZhOf6puHwhYwmdrt3v0XurDqRRNNZrAliErQ" http://127.0.0.1:8000/count
{"successful_requests":123,"requested_by":"alice"}[root@localhost ~]#
```
