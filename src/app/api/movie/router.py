from fastapi import APIRouter, Depends
# from src.auth.auth import redis
from src.auth.manager import current_user
from src.models import User

router = APIRouter()


@router.get("/")
async def protected_route(
    user: User = Depends(current_user())
):
    return {"msg": "Success"}
