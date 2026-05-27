from app.db.database import SessionLocal
from app.models.product import Product


db = SessionLocal()

existing = db.query(Product).count()

if existing == 0:

    db.add_all([
        Product(
            name="Laptop",
            price=50000,
            stock_quantity=20
        ),

        Product(
            name="Phone",
            price=25000,
            stock_quantity=50
        )
    ])

    db.commit()

print("seed completed")