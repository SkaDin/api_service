from datetime import date
from typing import Optional, Tuple
from decimal import Decimal

from pydantic import BaseModel, Field


class CreateMovie(BaseModel):
    title_en: str = Field(max_length=60)
    title_ru: str = Field(max_length=60)
    poster: Optional[str]
    description: str
    genre: Tuple[str, ...]
    country: Tuple[str, ...] = Field(max_length=60)
    slogan: Optional[str]
    rating: Decimal
    age_limit: str = Field(max_length=3)
    original_language: Tuple[str, ...]
    release_year: date
    actors: int  # TODO понять работу с M2M в pydantic
    directors: int
    source: str
    trailer: str
    duration: str = Field(max_length=3)
    budget: int
    fees: int


class OutMovie(CreateMovie):
    pass
