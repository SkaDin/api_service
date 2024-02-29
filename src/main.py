from fastapi import FastAPI

from src.app import router
from src.auth import auth_router


app = FastAPI()

app.include_router(router)
app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", port=8000, log_level="info")
