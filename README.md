# Ecommerce Order Engine

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)

Ecommerce backend built with FastAPI, PostgreSQL, Redis, Celery, and Docker using asynchronous event-driven architecture patterns for scalable order processing, inventory synchronization, caching, and analytics.

---

## Features

### Authentication & Authorization

* JWT-based authentication
* User registration & login
* Role-based access control
* Admin-protected product operations

### Product & Inventory System

* Product CRUD & inventory management
* Real-time stock validation and deduction
* Protected admin routes

### Async Order Processing

* Celery worker-based background processing
* Redis queue integration
* Retry handling for failed tasks
* Inventory synchronization
* Order lifecycle tracking: `PENDING` → `CONFIRMED` → `FAILED`

### Analytics Engine

* Revenue tracking
* Top-selling products
* Orders-by-day aggregation
* Failure-rate monitoring
* Redis-cached analytics endpoints

### Other Features

* Dockerized multi-service architecture
* Structured logging
* Global exception handling
* Environment-based configuration
* Seed data script
* Swagger API documentation

---

## System Architecture

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

## Tech Stack

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Core programming language  |
| FastAPI    | API framework              |
| PostgreSQL | Relational database        |
| SQLAlchemy | ORM                        |
| Redis      | Queue & caching            |
| Celery     | Background task processing |
| Docker     | Containerization           |
| JWT        | Authentication             |
| Pydantic   | Validation & schemas       |

---

## Project Structure

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

## Requirements

* Docker
* Docker Compose
* Python 3.11+

---

## Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/faraiz88/Ecommerce-Order-Engine.git
cd ecommerce-order-engine
```

### 2. Create `.env`

```env
DATABASE_URL=postgresql://username:password@db:5432/ecommerce_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
REDIS_URL=redis://redis:6379/0
```

### 3. Run the System

```bash
docker compose up --build
```

### 4. Seed Demo Data

```bash
docker compose exec api python -m scripts.seed
```

### 5. Health Check

```
GET /health  →  { "status": "ok" }
```

---

## Deployment

**Live API:** `https://ecommerce-order-engine-production.up.railway.app`

**Swagger Docs:** `https://ecommerce-order-engine-production.up.railway.app/docs`

Deployed on Railway with Docker-based containerization. Local Swagger UI available at `http://localhost:8000/docs`.

---

## API Endpoints

### Authentication

| Method | Endpoint         |
| ------ | ---------------- |
| POST   | `/auth/register` |
| POST   | `/auth/login`    |

Protected routes use JWT Bearer tokens. After login, use `Authorize → Bearer <token>` in Swagger UI.

### Products

| Method | Endpoint               |
| ------ | ---------------------- |
| GET    | `/products`            |
| GET    | `/products/{id}`       |
| POST   | `/products`            |
| PUT    | `/products/{id}`       |
| PATCH  | `/products/{id}/stock` |

### Orders

| Method | Endpoint            |
| ------ | ------------------- |
| POST   | `/orders`           |
| GET    | `/orders/{id}`      |
| GET    | `/orders/my-orders` |

### Analytics

| Method | Endpoint                   |
| ------ | -------------------------- |
| GET    | `/analytics/summary`       |
| GET    | `/analytics/top-products`  |
| GET    | `/analytics/orders-by-day` |
| GET    | `/analytics/failure-rate`  |

---

## Order Processing Flow

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

## Known Limitations / Planned

* No payment gateway integration yet
* Celery beat not configured for scheduled/recurring tasks
* No email notifications on order status changes

---

## License

MIT License

---

## Author

Mohammed Faraiz
