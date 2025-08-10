
# Bonus

## 6.1 Diagrama arquitetônico

<img width="1536" height="1024" alt="ChatGPT Image 10 авг  2025 г , 21_45_00" src="https://github.com/user-attachments/assets/bfde08a0-3b6c-4191-bc4c-01a0d2f5566f" />


6.2 Бэкенд
Использовать FastAPI (Python) или Nest.js (Node.js)

Выбрать СУБД — лучше PostgreSQL для сложных запросов и ACID

Имплементировать REST API (счётчик успешных запросов)

6.3 Логи
Логи писать в stdout (для контейнеров)

Подключить Fluentd/Fluent Bit или просто описать, где смотреть логи (kubectl logs <pod>)

6.4 Тесты
Unit tests: для FastAPI — pytest + тестовый клиент; для Nest.js — Jest

E2E tests: Pytest с requests для FastAPI, или Cypress для Node.js

6.5 Рефакторинг
Если есть базовый код — проверить на антипаттерны, убрать дублирование, добавить документацию

6.6 DevOps, SecOps, FinOps
Подробно описать и реализовать (мы это уже сделали)

6.7 Аутентификация / Авторизация
Добавить JWT или OAuth2 (FastAPI отлично поддерживает OAuth2 с Password flow)

Сделать защиту эндпоинтов

6.8 Мониторинг
Добавить Prometheus metrics в приложение

Настроить Grafana дашборд (примерно описать)

6.9 Деплой
Развернуть в Google Cloud (GKE или Cloud Run)

Предоставить ссылку на работающий сервис (если хочешь — могу помочь с деплоем)

Что предлагаю сделать сейчас?
Сформировать архитектурную диаграмму (в Mermaid или PlantUML)

Подготовить пример JWT-аутентификации для FastAPI

Написать пример unit и e2e тестов для backend

Описать, где смотреть логи и как их собирать

Если хочешь, помочь с деплоем в Google Cloud и составить инструкции
