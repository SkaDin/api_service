from fastapi import APIRouter, Depends, HTTPException
# from fastapi.encoders import jsonable_encoder
#
# from sqlalchemy import insert, select, cast, func, Integer, and_, String, Result, any_
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import joinedload, selectinload
#
# from src.app.api.v1.schemas import CreateMovie, OutMovie, ActorView
# from src.core.db import get_async_session
# from src.models.movie import Movie, Actor, Director


router = APIRouter()


@router.get(
    "/",
)
async def get_data(
):
    pass


@router.post(
    "/",
)
async def create_movie(
) -> dict:
    pass
