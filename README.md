# Ecommerce Order Engine

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Redis](https://img.shields.io/badge/Redis-Queue-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

A production-style ecommerce backend built using asynchronous event-driven architecture patterns with FastAPI, Celery, Redis, PostgreSQL, and Docker to simulate how scalable commerce platforms handle authentication, inventory synchronization, distributed task processing, caching, and business analytics in real-world environments.

---

# 📌 Purpose

This project was built to demonstrate production-grade backend engineering concepts commonly used in scalable ecommerce systems, including asynchronous workflows, distributed task queues, caching strategies, inventory consistency handling, analytics aggregation, and containerized deployment architecture.

---

# 🚀 Features

## Authentication & Authorization
- JWT-based authentication
- User registration & login
- Role-based access control
- Admin-only product management

---

## Product & Inventory System
- Product CRUD APIs
- Inventory management
- Stock validation
- Real-time stock deduction
- Protected admin routes

---

## Async Order Processing
- Orders processed asynchronously using Celery workers
- Redis queue integration
- Background task execution
- Retry mechanism for failed tasks
- Inventory synchronization handling
- Order lifecycle tracking:
  - `PENDING`
  - `CONFIRMED`
  - `FAILED`

---

## Analytics Engine
Business intelligence endpoints for:
- Revenue tracking
- Top-selling products
- Orders by day
- Failure-rate monitoring
- Cached analytics using Redis

---

## Production Features
- Dockerized multi-service architecture
- Structured logging
- Global exception handling
- Environment-based configuration
- Seed data script
- Swagger API documentation
- Health monitoring endpoint

---

# 🧠 System Architecture

```text
                +------------------+
                |      Client      |
                +------------------+
                          |
                          v
                +------------------+
                |   FastAPI API    |
                +------------------+
                   |           |
                   v           v
         +---------------+   +---------------+
         | PostgreSQL DB |   | Redis Queue   |
         +---------------+   +---------------+
                                      |
                                      v
                             +----------------+
                             | Celery Worker  |
                             +----------------+
                                      |
                                      v
                             +----------------+
                             | Analytics Layer|
                             +----------------+
```

---

# 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Redis | Queue + caching |
| Celery | Background task processing |
| Docker | Containerization |
| JWT | Authentication |
| Pydantic | Validation & schemas |

---

# 📂 Project Structure

```text
Ecommerce-Order-Engine/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── tasks/
│   └── main.py
│
├── scripts/
│   └── seed.py
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env
```

---

# ✅ Requirements

- Docker
- Docker Compose
- Python 3.11+

---

# ⚡ Quick Start

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-order-engine.git
cd ecommerce-order-engine
```

---

## 2. Create `.env`

```env
DATABASE_URL=postgresql://username:password@db:5432/ecommerce_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

REDIS_URL=redis://redis:6379/0
```

---

## 3. Run Entire System

```bash
docker compose up --build

```
---

# 🌐 Deployment

Live API deployment:

```text
https://ecommerce-order-engine-production.up.railway.app
```

Swagger Documentation:

```text
https://ecommerce-order-engine-production.up.railway.app/docs
```

Deployed using Railway with Docker-based containerization.

---

# 📘 API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

---

# ❤️ Core API Endpoints

## Authentication

| Method | Endpoint |
|---|---|
| POST | `/auth/register` |
| POST | `/auth/login` |

---

## Products

| Method | Endpoint |
|---|---|
| GET | `/products` |
| GET | `/products/{id}` |
| POST | `/products` |
| PUT | `/products/{id}` |
| PATCH | `/products/{id}/stock` |

---

## Orders

| Method | Endpoint |
|---|---|
| POST | `/orders` |
| GET | `/orders/{id}` |
| GET | `/orders/my-orders` |

---

## Analytics

| Method | Endpoint |
|---|---|
| GET | `/analytics/summary` |
| GET | `/analytics/top-products` |
| GET | `/analytics/orders-by-day` |
| GET | `/analytics/failure-rate` |

---

# 🔄 Order Processing Flow

```text
User places order
        ↓
Order stored as PENDING
        ↓
Task pushed to Redis queue
        ↓
Celery worker consumes task
        ↓
Inventory validated
        ↓
Stock deducted
        ↓
Order marked CONFIRMED or FAILED
```

---

# 📊 Analytics Capabilities

The analytics engine provides:
- Revenue aggregation
- Product sales metrics
- Time-based order tracking
- Failure monitoring
- Redis caching for improved performance

---

# 🧪 Seed Demo Data

Run:

```bash
docker compose exec api python -m scripts.seed
```

---

# 🩺 Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

# 🔐 Authentication

Protected routes use JWT Bearer authentication.

After login:

```text
Authorize → Bearer <token>
```

inside Swagger UI.

---

# 🐳 Docker Services

| Service | Description |
|---|---|
| api | FastAPI backend |
| db | PostgreSQL database |
| redis | Redis queue & caching |
| worker | Celery background worker |

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Mohammed Faraiz
