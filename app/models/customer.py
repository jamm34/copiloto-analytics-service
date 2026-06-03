from sqlalchemy import Integer, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from datetime import datetime


class Customer(Base):
    __tablename__ = "Customers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    fullName: Mapped[str] = mapped_column(Text)

    email: Mapped[str] = mapped_column(Text)

    phone: Mapped[str] = mapped_column(Text)

    city: Mapped[str] = mapped_column(Text)

    country: Mapped[str] = mapped_column(Text)

    registrationDate: Mapped[datetime] = mapped_column(DateTime)

    segment: Mapped[str] = mapped_column(Text)

    status: Mapped[str] = mapped_column(Text)

    frequency: Mapped[str] = mapped_column(Text)

    lastPurchase: Mapped[int] = mapped_column(Integer)

    interest: Mapped[str] = mapped_column(Text)

    orders = relationship(
        "Order",
        back_populates="customer"
    )