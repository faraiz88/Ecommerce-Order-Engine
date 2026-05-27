from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import get_db
from sqlalchemy import cast, Date
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.core.logger import logger
from app.core.dependencies import require_admin
from app.services.cache import get_cache, set_cache


router = APIRouter(
    prefix="/analytics",
    tags=["analytics"]
)


@router.get("/summary")
def summary(
    db: Session = Depends(get_db),
    user=Depends(require_admin)
):

    cached = get_cache(
        "analytics_summary"
    )

    if cached:
        return cached

    total_orders = (
        db.query(Order)
        .count()
    )

    confirmed = (
        db.query(Order)
        .filter(
            Order.status ==
            "CONFIRMED"
        )
        .count()
    )

    failed = (
        db.query(Order)
        .filter(
            Order.status ==
            "FAILED"
        )
        .count()
    )

    revenue = (
        db.query(
            func.sum(
                OrderItem.quantity
                *
                OrderItem.price_at_purchase
            )
        )
        .scalar()
    )

    result = {
        "total_orders":
        total_orders,

        "confirmed":
        confirmed,

        "failed":
        failed,

        "revenue":
        revenue or 0
    }

    set_cache(
        "analytics_summary",
        result
    )

    logger.info(
        "Analytics summary generated"
    )

    return result


@router.get("/top-products")
def top_products(
    db: Session = Depends(get_db),
    user=Depends(require_admin)
):

    rows = (
        db.query(
            Product.name,
            func.sum(
                OrderItem.quantity
            ).label(
                "units"
            )
        )

        .join(
            OrderItem,
            Product.id
            ==
            OrderItem.product_id
        )

        .group_by(
            Product.name
        )

        .order_by(
            func.sum(
                OrderItem.quantity
            ).desc()
        )

        .limit(5)

        .all()
    )

    return [
        {
            "product":
            r[0],

            "units_sold":
            r[1]
        }

        for r in rows
    ]


@router.get("/orders-by-day")
def orders_by_day(
    db: Session = Depends(get_db),
    user=Depends(require_admin)
):

    rows = (
        db.query(
            cast(
                Order.created_at,
                Date
            ).label(
                "day"
            ),

            func.count(
                Order.id
            )
        )

        .group_by(
            cast(
                Order.created_at,
                Date
            )
        )

        .order_by(
            cast(
                Order.created_at,
                Date
            )
        )

        .all()
    )

    return [
        {
            "date": str(r[0]),
            "orders": r[1]
        }

        for r in rows
    ]


@router.get("/failure-rate")
def failure_rate(
    db: Session = Depends(get_db),
    user=Depends(require_admin)
):

    total = (
        db.query(Order)
        .count()
    )

    failed = (
        db.query(Order)
        .filter(
            Order.status ==
            "FAILED"
        )
        .count()
    )

    rate = 0

    if total:
        rate = round(
            (
                failed
                / total
            ) * 100,
            2
        )

    return {
        "total_orders":
        total,

        "failed_orders":
        failed,

        "failure_rate_percent":
        rate
    }