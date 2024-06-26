from datetime import datetime
from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy import String, text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column
from fastapi_users.db import SQLAlchemyUserDatabase
from src.core.config import settings


str_256 = Annotated[str, 256]

str_3 = Annotated[str, 3]

int_pk = Annotated[int, mapped_column(primary_key=True)]

create_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())")
)]

update_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow
)]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256),
        str_3: String(3)
    }


engine = create_async_engine(settings.DB_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as async_session:
        yield async_session


async def get_user_db(
    session: AsyncSession = Depends(get_async_session),
):
    from src.models import User  # ignore cyclic import
    yield SQLAlchemyUserDatabase(session, User)
