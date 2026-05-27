from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.schemas.order import OrderCreate, OrderResponse
from app.core.dependencies import get_current_user
from app.models.user import User
from app.services.inventory import reduce_stock
from app.tasks.order_tasks import process_order
from app.core.logger import logger



router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@router.post(
    "/",
    response_model=OrderResponse
)
def create_order(
    body: OrderCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):

    if not body.items:
        raise HTTPException(
            400,
            "Order must contain at least one item"
        )

    seen = set()

    for item in body.items:

        if item.product_id in seen:
            raise HTTPException(
                400,
                "Duplicate product in order"
            )

        seen.add(item.product_id)

    order = Order(
        user_id=user.id,
        status="PENDING"
    )

    db.add(order)

    db.commit()

    db.refresh(order)

    logger.info(
        f"Order created | id={order.id} user={user.id}"
    )

    process_order.delay(
        order.id,
        [
            i.model_dump()
            for i in body.items
        ]
    )

    return order


@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):

    order = (
        db.query(Order)
        .filter(
            Order.id == order_id
        )
        .first()
    )

    if not order:
        raise HTTPException(
            404,
            "Order not found"
        )

    if (
        order.user_id != user.id
        and user.role != "admin"
    ):
        raise HTTPException(
            403,
            "Access denied"
        )

    return order