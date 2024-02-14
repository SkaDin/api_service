from fastapi import FastAPI

from src.app import router


app = FastAPI()

app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", port=8000, log_level="info")
