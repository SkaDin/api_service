from datetime import date
from typing import Optional

from sqlalchemy import (
    ForeignKey,
    String,
    Text,
    ARRAY,
    Date,
    DECIMAL, Index,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from src.core.db import Base, str_256, int_pk, create_at, update_at, str_3
from src.models.director import Director
from src.models import Actor


class Movie(Base):
    __tablename__ = "movie"
    id: Mapped[int_pk]
    title_ru: Mapped[str_256]
    title_en: Mapped[str_256]
    poster: Mapped[Optional[str]]
    description: Mapped[str] = mapped_column(Text)
    genre: Mapped[str] = mapped_column(ARRAY(String(256)))
    country: Mapped[str] = mapped_column(ARRAY(String(256)))
    directors: Mapped[list["Director"]] = relationship(
        "Director",
        back_populates="movies_directors",
        secondary="movie_director_association",
    )
    actors: Mapped[list["Actor"]] = relationship(
        "Actor",
        back_populates="movies_actors",
        secondary="movie_actor_association",
    )
    slogan: Mapped[Optional[str]]
    rating: Mapped[DECIMAL] = mapped_column(
        DECIMAL(scale=1, precision=2), default=0.0
    )
    age_limit: Mapped[str_3]
    original_language: Mapped[str_256]
    release_year: Mapped[date] = mapped_column(Date)
    create_at: Mapped[create_at]
    update_at: Mapped[update_at]
    source: Mapped[str]
    trailer: Mapped[str]
    duration: Mapped[str]
    budget: Mapped[str]
    fees: Mapped[str]

    __table_args__ = (
        Index("title_index", "title_ru", "title_en"),
    )
