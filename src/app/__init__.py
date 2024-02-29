from fastapi import APIRouter

from src.app.api.movie.router import router as create_router

router = APIRouter(prefix="/api/v1")

router.include_router(create_router)
