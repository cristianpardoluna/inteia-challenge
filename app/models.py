import uuid
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .db import Base

class Book(Base):
    __tablename__ = "libros"

    id: Mapped[int] = mapped_column(
        String(36),
        name="isbn",
        primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)
