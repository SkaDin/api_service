from datetime import date
from typing import List

from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base, str_256
from src.models.many_to_many_table import movie_director_association


class Director(Base):
    __tablename__ = "director"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    date_of_birth: Mapped[date] = mapped_column(Date)
    movies: Mapped[List["Movie"]] = relationship(  # noqa cyclic import
        "Movie",
        secondary=movie_director_association,
        back_populates="directors",
    )
