from datetime import date

from sqlalchemy import Date, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import Base, str_256


class Director(Base):
    __tablename__ = "director"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    date_of_birth: Mapped[date] = mapped_column(Date)
    movies_directors: Mapped[list["Movie"]] = relationship(  # noqa cyclic import
        "Movie",
        back_populates="directors",
        secondary="movie_director_association",
    )

    __table_args__ = (
        Index("first_name_index_to_director", "first_name"),
    )
