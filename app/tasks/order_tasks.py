from app.core.celery_app import celery
from app.db.session import get_db
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.core.logger import logger
from app.services.inventory import reduce_stock


@celery.task(
    bind=True,
    max_retries=3
)
def process_order(
    self,
    order_id: int,
    items: list
):

    db = next(get_db())

    order = None

    try:

        order = (
            db.query(Order)
            .filter(
                Order.id == order_id
            )
            .first()
        )

        if not order:
            return

        for item in items:

            product = (
                db.query(Product)
                .filter(
                    Product.id ==
                    item["product_id"]
                )
                .first()
            )

            if not product:
                raise Exception(
                    "Product not found"
                )

            reduce_stock(
                product,
                item["quantity"]
            )

            db.add(
                OrderItem(
                    order_id=order.id,
                    product_id=product.id,
                    quantity=item["quantity"],
                    price_at_purchase=product.price
                )
            )

        order.status = (
            "CONFIRMED"
        )

        db.commit()

        logger.info(
            f"Order confirmed | id={order.id}"
        )

    except Exception as e:

        logger.error(
            f"Order processing failed | id={order_id} error={str(e)}"
        )

        db.rollback()

        if order:

            order.status = (
                "FAILED"
            )

            db.commit()

        raise self.retry(
            countdown=5
        )

    finally:

        db.close()