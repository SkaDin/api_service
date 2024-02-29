import pytest
import pytest_asyncio
from sqlalchemy import create_engine, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.asyncio import async_session
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

    # container.stop()


@pytest_asyncio.fixture(scope="session")
def test_db(postgres_container):

    engine = create_engine(
        # "postgresql+asyncpg://postgres:05111996@localhost:5433/test_my_db_proj",
        # connect_args={'check_same_thread': False},
        postgres_container.get_connection_url(),
        echo=True,
    )
    print(postgres_container.get_connection_url())
    with engine.begin() as conn:
        Base.metadata.create_all(bind=engine)

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
        stmt = session.execute(select(
            Movie
        ))
        res = stmt.scalars().all()
        assert res, "Nothing"
