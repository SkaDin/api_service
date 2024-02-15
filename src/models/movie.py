from datetime import date
from typing import Optional

from sqlalchemy import (
    ForeignKey,
    String,
    Text,
    ARRAY,
    Date,
    DECIMAL
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from src.core.db import Base, str_256, int_pk, create_at, update_at
from src.models.director import Director
from src.models import Actor
from src.models.many_to_many_table import (
    movie_director_association,
    movie_actor_association,
)


class Movie(Base):
    __tablename__ = "movie"
    id: Mapped[int_pk]
    title: Mapped[str_256]
    poster: Mapped[Optional[str]]
    description: Mapped[str] = mapped_column(Text)
    genre: Mapped[str] = mapped_column(ARRAY(String(256)))
    country: Mapped[str] = mapped_column(ARRAY(String(256)))
    directors: Mapped[list["Director"]] = relationship(
        "Director",
        secondary=movie_director_association,
        back_populates="movies",
    )
    actors: Mapped[list["Actor"]] = relationship(
        "Actor",
        secondary=movie_actor_association,
        back_populates="movies",
    )
    actor_id: Mapped[int] = mapped_column(ForeignKey("actor.id"))
    director_id: Mapped[int] = mapped_column(ForeignKey("director.id"))
    slogan: Mapped[Optional[str]]
    rating: Mapped[DECIMAL] = mapped_column(
        DECIMAL(scale=2, precision=3), default=0.00
    )
    age_limit: Mapped[str] = mapped_column(String(3))
    language: Mapped[Optional[str]] = mapped_column(ARRAY(String(256)))
    release_year: Mapped[date] = mapped_column(Date)
    create_at: Mapped[create_at]
    update_at: Mapped[update_at]
    source: Mapped[str]
    trailer: Mapped[str]
