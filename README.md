# Ecommerce Order Engine

A production-style asynchronous ecommerce backend built with **Python**, **FastAPI**, **PostgreSQL**, **Redis**, **Celery**, and **Docker**.

This project is a production-style ecommerce backend system designed to demonstrate how scalable commerce platforms handle authentication, inventory management, asynchronous order processing, distributed task queues, caching, and business analytics in real-world environments.

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
- Orders processed in background using Celery
- Redis queue integration
- Async stock handling
- Retry mechanism for failures
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
- Dockerized architecture
- Structured logging
- Global error handling
- Seed data script
- Swagger API documentation
- Health check endpoint

---

# 🧠 Final Architecture

```text
Client
↓
FastAPI API Layer
↓
PostgreSQL Database
↓
Redis (Queue + Cache)
↓
Celery Workers
↓
Analytics Layer
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
Task sent to Redis queue
↓
Celery worker processes order
↓
Inventory validated
↓
Stock deducted
↓
Order CONFIRMED or FAILED
```

---

# 📊 Analytics Capabilities

The analytics layer provides:
- Revenue aggregation
- Product sales metrics
- Time-based order tracking
- Failure monitoring
- Redis caching for performance

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

Protected routes use JWT Bearer tokens.

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
| redis | Redis queue/cache |
| worker | Celery worker |

---

# 📈 Skills Demonstrated

- Backend API development
- Asynchronous systems
- Queue-based architectures
- Inventory management
- Database modeling
- Analytics aggregation
- Docker containerization
- Production-ready backend design

---

# 🎯 Project Status

```text
Phase 1 — Authentication ✅
Phase 2 — User System ✅
Phase 3 — Product & Inventory ✅
Phase 4 — Order Management ✅
Phase 5 — Async Processing ✅
Phase 6 — Analytics Engine ✅
Phase 7 — Productionization ✅
```

---

# 👨‍💻 Author

Mohammed Faraiz
