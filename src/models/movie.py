from datetime import datetime
from typing import Optional, List

from sqlalchemy import (
    ForeignKey,
    String,
    Text,
    Enum,
    ARRAY,
    Integer,
    Date,
    DECIMAL,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)
from src.core.enums import GenreMovie
from src.core.db import Base


class Actor(Base):
    __tablename__ = "actor"
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String(255), nullable=True)
    date_of_birth: Mapped[datetime] = mapped_column(Date, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    country: Mapped[str] = mapped_column(String(50), nullable=False)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    movie: Mapped["Movie"] = relationship(back_populates="actor")


class Movie(Base):
    __tablename__ = "movie"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(60), nullable=False)
    poster: Mapped[Optional[str]]
    description: Mapped[str] = mapped_column(Text, nullable=False)
    genre: Mapped[str] = mapped_column(Enum(GenreMovie), nullable=False)
    country: Mapped[str] = mapped_column(ARRAY(String(50)), nullable=False)
    director: Mapped[str] = mapped_column(ARRAY(String(50)), nullable=False)
    actor_id: Mapped[List["Actor"]] = relationship(back_populates="movie")
    slogan: Mapped[Optional[str]]
    rating: Mapped[DECIMAL] = mapped_column(
        DECIMAL(scale=2, precision=3), nullable=False, default=0.00
    )
    age_limit: Mapped[str] = mapped_column(String(3))
    language: Mapped[Optional[str]]
