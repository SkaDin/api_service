from datetime import date
from typing import Optional, List

from sqlalchemy import (
    ForeignKey,
    String,
    Text,
    Enum,
    ARRAY,
    Integer,
    Date,
    DECIMAL, Table, Column,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from src.core.enums import GenreMovie
from src.core.db import Base


movie_actor_association = Table(
    "movie_actor_association",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movie.id")),
    Column("actor_id", Integer, ForeignKey("actor.id")),
)

movie_director_association = Table(
    "movie_director_association",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movie.id")),
    Column("director_id", Integer, ForeignKey("director.id")),
)


class Movie(Base):
    __tablename__ = "movie"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(60), nullable=False)
    poster: Mapped[Optional[str]]
    description: Mapped[str] = mapped_column(Text, nullable=False)
    genre: Mapped[str] = mapped_column(Enum(GenreMovie), nullable=False)
    country: Mapped[str] = mapped_column(ARRAY(String(50)), nullable=False)
    directors: Mapped[List["Director"]] = relationship(
        "Director",
        secondary=movie_director_association,
        back_populates="movies",
    )
    actors: Mapped[List["Actor"]] = relationship(
        "Actor",
        secondary=movie_actor_association,
        back_populates="movies",
    )
    actor_id: Mapped[int] = mapped_column(ForeignKey("actor.id"))
    director_id: Mapped[int] = mapped_column(ForeignKey("director.id"))
    slogan: Mapped[Optional[str]]
    rating: Mapped[DECIMAL] = mapped_column(
        DECIMAL(scale=2, precision=3), nullable=False, default=0.00
    )
    age_limit: Mapped[str] = mapped_column(String(3))
    language: Mapped[Optional[str]] = mapped_column(ARRAY(String(30)))
    release_year: Mapped[date] = mapped_column(Date)


class Actor(Base):
    __tablename__ = "actor"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), nullable=True)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    country: Mapped[str] = mapped_column(String(50), nullable=False)
    movies: Mapped["Movie"] = relationship(
        "Movie",
        secondary=movie_actor_association,
        back_populates="actors",
    )


class Director(Base):
    __tablename__ = "director"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), nullable=True)
    date_of_birth: Mapped[date] = mapped_column(Date)
    movies: Mapped[List["Movie"]] = relationship(
        "Movie",
        secondary=movie_director_association,
        back_populates="directors",
    )

