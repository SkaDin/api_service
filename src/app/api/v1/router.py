from fastapi import APIRouter, Depends

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.api.v1.schemas import CreateMovie
from src.core.db import get_async_session
from src.models.movie import Movie


router = APIRouter()


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
