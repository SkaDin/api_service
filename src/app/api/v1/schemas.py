from datetime import date
from typing import Optional, Tuple
from decimal import Decimal

from pydantic import BaseModel, Field


class ActorView(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_of_birth: date
    age: int
    country: str


class DirectorView(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_of_birth: date


class CreateMovie(BaseModel):
    title_en: str = Field(max_length=60)
    title_ru: str = Field(max_length=60)
    poster: Optional[str]
    description: str
    genre: list[str]
    country: list[str] = Field(max_length=60)
    slogan: Optional[str]
    rating: Decimal
    age_limit: str = Field(max_length=3)
    original_language: str
    release_year: date
    actors: list[ActorView]
    directors: list[DirectorView]
    source: str
    trailer: str
    duration: str
    budget: int
    fees: int


class OutMovie(CreateMovie):
    pass
