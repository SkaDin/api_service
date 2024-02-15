from datetime import date

from sqlalchemy import Date, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base, str_256, int_pk

from src.models.many_to_many_table import movie_actor_association


class Actor(Base):
    __tablename__ = "actor"
    id: Mapped[int_pk]
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    date_of_birth: Mapped[date] = mapped_column(Date)
    age: Mapped[int] = mapped_column(Integer)
    country: Mapped[str_256]
    movies: Mapped["Movie"] = relationship( # noqa cyclic import
        "Movie",
        secondary=movie_actor_association,
        back_populates="actors",
    )

