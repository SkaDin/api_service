from datetime import date
from typing import Optional, Tuple
from decimal import Decimal

from pydantic import BaseModel, Field

from src.core.enums import GenreMovie


class CreateMovie(BaseModel):
    title: str = Field(max_length=60)  # alias="Название"
    poster: Optional[str]  # = Field(alias="Постер")
    description: str  # = Field(alias="Краткое описание")
    genre: Tuple[GenreMovie, ...]  # = Field(alias="Жанр") # TODO решить вопрос с pydantic
    country: Tuple[str, ...] = Field(max_length=60)  # alias="Страна производства"
    slogan: Optional[str]  # = Field(alias="Слоган")
    rating: Decimal  # = Field(alias="Рейтинг")
    age_limit: str = Field(max_length=3)  # alias="Возрастное ограничение",
    language: Tuple[str, ...]  # = Field(alias="Озвучки")
    release_year: date  # = Field(alias="Дата выхода")
