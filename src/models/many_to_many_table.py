from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db import Base


class MovieActorAssociation(Base):
    __tablename__ = "movie_actor_association"
    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movie.id", ondelete="CASCADE"),
        primary_key=True,
    )
    actor_id: Mapped[int] = mapped_column(
        ForeignKey("actor.id", ondelete="CASCADE"),
        primary_key=True,
    )
    UniqueConstraint(
        'movie_id', 'actor_id', name='uq_movie_actor_association',
    )


class MovieDirectorAssociation(Base):
    __tablename__ = "movie_director_association"

    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movie.id", ondelete="CASCADE"),
        primary_key=True,
    )
    director_id: Mapped[int] = mapped_column(
        ForeignKey("director.id", ondelete="CASCADE"),
        primary_key=True,
    )
    UniqueConstraint(
        'movie_id', 'director_id', name='uq_movie_director_association',
    )
