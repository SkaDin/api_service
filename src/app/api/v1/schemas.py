from datetime import date
from typing import Optional, Tuple
from decimal import Decimal

from pydantic import BaseModel, Field


class CreateMovie(BaseModel):
    title: str = Field(max_length=60)
    poster: Optional[str]
    description: str
    genre: Tuple[str, ...] = Field(default=["Unknown"])
    country: Tuple[str, ...] = Field(max_length=60)
    slogan: Optional[str]
    rating: Decimal
    age_limit: str = Field(max_length=3)
    language: Tuple[str, ...]
    release_year: date
    actor_id: int = Field(default=1)
    director_id: int = Field(default=1)
    source: Optional[str]
    trailer: Optional[str]


class OutMovie(CreateMovie):
    pass