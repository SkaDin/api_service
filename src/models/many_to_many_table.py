from sqlalchemy import Table, Column, Integer, ForeignKey

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
