import datetime

from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import Text
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import ForeignKey

from app.models.base import Base

class Order(Base):

    __tablename__ = "Orders"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    customerId: Mapped[int] = mapped_column(
        ForeignKey("Customers.id")
    )

    totalAmount: Mapped[float] = mapped_column(
        Numeric
    )

    orderDate: Mapped[datetime] = mapped_column(
        DateTime
    )

    status: Mapped[str] = mapped_column(
        Text
    )

    salesUserId: Mapped[str] = mapped_column(
        Text
    )

    customer = relationship(
        "Customer",
        back_populates="orders"
    )

    items = relationship(
        "OrderItem",
        back_populates="order"
    )