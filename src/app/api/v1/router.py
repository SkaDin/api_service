from fastapi import APIRouter, Depends

from src.app.api.v1.schemas import CreateMovie

router = APIRouter()


@router.post(
    "/",
)
async def create_movie(
    data: CreateMovie,
) -> dict:

    return {"msg": "Success"}
