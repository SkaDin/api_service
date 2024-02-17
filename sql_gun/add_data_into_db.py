import asyncio

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text


engine = create_async_engine("postgresql+asyncpg://postgres:05111996@localhost:5433/my_db_proj")


async def add_sql_scripts():
    paths = (
        "sql_gun/pg/insert_actors.sql",
        "sql_gun/pg/insert_directors.sql",
        "sql_gun/pg/insert_movie.sql",
    )
    for path in paths:
        with open(path, "r") as file:
            script = file.read()

        async with engine.begin() as connection:
            await connection.execute(text(script))

asyncio.run(add_sql_scripts())
