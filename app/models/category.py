from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class Category(Base):

    __tablename__ = "Categories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        Text
    )

    description: Mapped[str] = mapped_column(
        Text
    )