from fastapi import APIRouter, Depends

from sqlalchemy import insert, select
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
) -> OutMovie:
    query = await session.execute(
        select(Movie)
        .where(Movie.actor_id == Actor.id)
    )
    qeury2 = await session.get(Movie, movie_id)
    res = query.scalar().__dict__
    print(f"\n\n\n\n{qeury2}\n\n\n")
    return res


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
    print(f"")
    await session.flush()
    await session.commit()

    return {"msg": "Success"}
