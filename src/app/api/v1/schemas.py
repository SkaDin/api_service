from datetime import date
from typing import Optional
from decimal import Decimal

from pydantic import BaseModel, Field

from src.core.enums import GenreMovie


class CreateMovie(BaseModel):
    title: str = Field(alias="Название", max_length=60)
    poster: Optional[str]
    descriptions: str = Field(alias="Краткое описание")
    genre: GenreMovie = Field(alias="Жанр")
    country: list[str] = Field(max_length=60, alias="Страна производства")
    slogan: Optional[str] = Field(alias="Слоган")
    rating: Decimal = Field(alias="Рейтинг")
    age_limit: str = Field(alias="Возрастное ограничение", max_length=3)
    language: list[str] = Field(alias="Озвучки")
    release_year: date
