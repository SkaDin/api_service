from datetime import date, datetime
from typing import Annotated, Optional, List

from sqlalchemy import (
    ForeignKey,
    String,
    Text,
    Enum,
    ARRAY,
    Integer,
    Date,
    DECIMAL, Table, Column, text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from src.core.enums import GenreMovie
from src.core.db import Base, str_256


int_pk = Annotated[int, mapped_column(primary_key=True)]

create_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())")
)]

update_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow
)]


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
    id: Mapped[int_pk]
    title: Mapped[str_256]
    poster: Mapped[Optional[str]]
    description: Mapped[str] = mapped_column(Text)
    genre: Mapped[str] = mapped_column(Enum(GenreMovie))
    country: Mapped[str] = mapped_column(ARRAY(String(256)))
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
        DECIMAL(scale=2, precision=3), default=0.00
    )
    age_limit: Mapped[str] = mapped_column(String(3))
    language: Mapped[Optional[str]] = mapped_column(ARRAY(String(256)))
    release_year: Mapped[date] = mapped_column(Date)
    create_at: Mapped[create_at]
    update_at: Mapped[update_at]


class Actor(Base):
    __tablename__ = "actor"
    id: Mapped[int_pk]
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    date_of_birth: Mapped[date] = mapped_column(Date)
    age: Mapped[int] = mapped_column(Integer)
    country: Mapped[str_256]
    movies: Mapped["Movie"] = relationship(
        "Movie",
        secondary=movie_actor_association,
        back_populates="actors",
    )


class Director(Base):
    __tablename__ = "director"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    date_of_birth: Mapped[date] = mapped_column(Date)
    movies: Mapped[List["Movie"]] = relationship(
        "Movie",
        secondary=movie_director_association,
        back_populates="directors",
    )
