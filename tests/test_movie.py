import pytest
import pytest_asyncio
from sqlalchemy import create_engine, select, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import async_session
from sqlalchemy.orm import selectinload

from src.core.base import ( # noqa
    Base,
    Director,
    Actor,
    Movie,
    MovieActorAssociation,
    MovieDirectorAssociation,
)
# from src.core.db import engine
from src.core.config import settings
from testcontainers.postgres import PostgresContainer


@pytest_asyncio.fixture(scope="session")
def postgres_container() -> PostgresContainer:
    container = PostgresContainer(
        "postgres:latest",
        user="postgres",
        password="05111996",
        dbname="test_my_db_proj",
    )
    container.start()

    yield container

    container.stop()


@pytest_asyncio.fixture(scope="session")
def test_db(postgres_container):

    engine = create_engine(
        # "postgresql+asyncpg://postgres:05111996@localhost:5433/test_my_db_proj",
        # connect_args={'check_same_thread': False},
        postgres_container.get_connection_url(),
        echo=True,
    )
    print(postgres_container.driver)
    with engine.begin() as conn:
        Base.metadata.create_all(bind=engine)
        paths = [
            "sql_gun/pg/insert_actors.sql",
            "sql_gun/pg/insert_directors.sql",
            "sql_gun/pg/insert_movie.sql",
            "sql_gun/pg/relation_actor.sql",
            "sql_gun/pg/relation_director.sql",
        ]

        for path in paths:
            with open(path, "r") as file:
                script = file.read()

            conn.execute(text(script))

    yield engine

    with engine.begin() as conn:
        Base.metadata.drop_all(bind=engine)

# TestingSessionLocal = async_sessionmaker(
#     class_=AsyncSession, autocommit=False, autoflush=False, bind=test_db,
# )


# @pytest.fixture(autouse=True)
# async def init_db():
#     assert settings.MODE == "TEST"
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
#     yield
#
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)


@pytest.mark.asyncio
async def test_get(test_db):
    print(test_db)
    assert 1 == 1


@pytest.mark.asyncio
async def test_post(test_db):
    print(test_db)
    assert 2 == 2


@pytest.mark.asyncio
async def test_patch(test_db):
    with test_db.begin() as session:
        stmt = session.execute(
            select(
                Actor.first_name,
                Actor.age,
            )
        )
        res = stmt.unique().all()
        print(f"\n\n\n\n\n{res}")
        assert res, "Nothing"
