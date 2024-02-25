from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.app import router
from src.auth.auth import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.models import User


app = FastAPI()


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app.include_router(router)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", port=8000, log_level="info")
