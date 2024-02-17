from datetime import datetime
from typing import AsyncGenerator, Annotated

from sqlalchemy import String, text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column

from src.core.config import Settings


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

    def __repr__(self):
        cols = [f"{col}={getattr(self, col)}" for col in self.__table__.columns.keys()]
        return f"\n<{self.__class__.__name__} {' '.join(cols)}>\n"


engine = create_async_engine(Settings.DB_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as async_session:
        yield async_session
