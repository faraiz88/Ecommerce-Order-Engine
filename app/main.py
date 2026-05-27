from fastapi import FastAPI
from app.models.base import Base
from app.models.user import User
from app.db.database import engine
from app.api.auth import router
from app.models.product import Product
from app.api.products import router as product_router
from app.models.order import Order
from app.models.order_item import OrderItem
from app.api.orders import router as order_router
from app.api.analytics import router as analytics_router
from fastapi import HTTPException
from app.core.errors import (
    http_error,
    generic_error
)


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(analytics_router)
app.add_exception_handler(HTTPException, http_error)
app.add_exception_handler(Exception, generic_error)

@app.get("/")
def root():
    return {
        "message": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }