from fastapi import HTTPException


def validate_stock(available: int, requested: int):
    if requested <= 0:
        raise HTTPException(
            400,
            "Quantity must be greater than zero"
        )
    if available < requested:
        raise HTTPException(
            400,
            "Insufficient stock"
        )


def reduce_stock(product, quantity):
    validate_stock(
        product.stock_quantity,
        quantity
    )
    product.stock_quantity -= quantity