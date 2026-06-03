from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base

class OrderItem(Base):

    __tablename__ = "OrderItem"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    orderId: Mapped[int] = mapped_column(
        ForeignKey("Orders.id")
    )

    productId: Mapped[int] = mapped_column(
        ForeignKey("Products.id")
    )

    quantity: Mapped[int] = mapped_column(
        Integer
    )

    unitPrice: Mapped[float] = mapped_column(
        Numeric
    )

    order = relationship(
        "Order",
        back_populates="items"
    )

    product = relationship(
        "Product",
        back_populates="items"
    )