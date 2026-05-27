from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.user import User
from sqlalchemy import DateTime
from datetime import datetime, timezone


class Order(Base):

    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    status = Column(
        String,
        default="PENDING"
    )

    created_at = Column(
        DateTime,
        default=lambda:
        datetime.now(
            timezone.utc
        )
    )

    user = relationship(
        "User"
    )

    items = relationship(
        "OrderItem",
        back_populates="order"
    )