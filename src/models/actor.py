from datetime import date

from sqlalchemy import Date, Integer, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base, str_256, int_pk


class Actor(Base):
    __tablename__ = "actor"
    id: Mapped[int_pk]
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    date_of_birth: Mapped[date] = mapped_column(Date)
    age: Mapped[int] = mapped_column(Integer)
    country: Mapped[str_256]
    movies_actors: Mapped[list["Movie"]] = relationship( # noqa cyclic import
        "Movie",
        back_populates="actors",
        secondary="movie_actor_association",
    )

    __table_args__ = (
        Index("first_name_index_to_actor", "first_name"),
    )

