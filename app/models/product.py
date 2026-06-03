from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base

class Product(Base):

    __tablename__ = "Products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        Text
    )

    price: Mapped[float] = mapped_column(
        Numeric
    )

    stock: Mapped[int] = mapped_column(
        Integer
    )

    imageUrl: Mapped[str] = mapped_column(
        Text
    )

    rating: Mapped[float] = mapped_column(
        Numeric
    )

    category_id: Mapped[int] = mapped_column(
        Integer
    )

    items = relationship(
        "OrderItem",
        back_populates="product"
    )