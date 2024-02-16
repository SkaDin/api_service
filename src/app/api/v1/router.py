from fastapi import APIRouter, Depends

from sqlalchemy import insert, select, cast, func, Integer, and_, String
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.api.v1.schemas import CreateMovie, OutMovie
from src.core.db import get_async_session
from src.models.movie import Movie, Actor, Director


router = APIRouter()


@router.get(
    "/"
)
async def get_data(
    movie_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> dict:
    query = (
        select(
            Movie.title_ru,
            Actor.first_name,
            Director.first_name,
        )
        .select_from(Movie)
        .join(Actor, Actor.id == Movie.actors)
        .join(Director, Director.id == Movie.directors)
    )
    query = await session.execute(query)
    res = query.one_or_none()
    print(f"\n\n\n\n{res}\n\n\n")
    return {"res": [*res]}


@router.post(
    "/",
)
async def create_movie(
    data: CreateMovie,
    session: AsyncSession = Depends(get_async_session)
) -> dict:
    stmt: dict = {
        key: value
        for key, value in data.dict().items()
        if value is not None
    }
    await session.execute(
        insert(Movie)
        .values(stmt)
    )
    print(f"\n\n\n\n{stmt}\n\n\n")
    await session.flush()
    await session.commit()

    return {"msg": "Success"}

{
  "title_en": "Interstellar",
  "title_ru": "Интерстеллар",
  "poster": "NOne",
  "description": "Когда засуха, пыльные бури и вымирание растений приводят человечество к продовольственному кризису, коллектив исследователей и учёных отправляется сквозь червоточину (которая предположительно соединяет области пространства-времени через большое расстояние) в путешествие, чтобы превзойти прежние ограничения для космических путешествий человека и найти планету с подходящими для человечества условиями.",
  "genre": [
    "фантастика", "драма", "приключения"
  ],
  "country": [
    "США", "Великобритания", "Канада"
  ],
  "slogan": "NOne",
  "rating": 8.6,
  "age_limit": "18+",
  "original_language": [
    "English"
  ],
  "release_year": "2014-11-05",
  "actor_id": [
    2, 5
  ],
  "director_id": [
    2
  ],
  "source": "NOne",
  "trailer": "None",
  "duration": "169",
  "budget": 165000000,
  "fees": 715751038
}