from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.product import Product
from app.core.dependencies import require_admin
from app.schemas.product import ProductUpdate
from app.core.logger import logger
from app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductStockUpdate
)


router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(require_admin)
):

    if product.stock_quantity < 0:
        raise HTTPException(400, "Invalid stock")
    obj = Product(
        name=product.name,
        price=product.price,
        stock_quantity=product.stock_quantity
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)
    logger.info(
        f"Product created | id={obj.id}"
    )
    return obj


@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.patch("/{product_id}/stock")
def update_stock(
    product_id: int,
    body: ProductStockUpdate,
    db: Session = Depends(
        get_db
    ),
    user=Depends(
        require_admin
    )
):

    product = (
        db.query(Product)
        .filter(
            Product.id == product_id
        )
        .first()
    )
    if not product:
        raise HTTPException(404,"Product not found")

    if body.stock_quantity < 0:
        raise HTTPException(400, "Stock cannot be negative")

    product.stock_quantity = (body.stock_quantity)
    db.commit()
    logger.info(
        f"Stock updated | product={product.id}"
    )
    db.refresh(product)
    return product



@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )
    if not product:
        raise HTTPException(
            404,
            "Product not found"
        )
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    body: ProductUpdate,
    db: Session = Depends(get_db),
    user=Depends(require_admin)
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )
    if not product:
        raise HTTPException(
            404,
            "Product not found"
        )
    data = body.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product


