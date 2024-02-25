from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db import Base, str_256, create_at


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str_256]
    first_name: Mapped[str_256]
    last_name: Mapped[str_256]
    registered_at: Mapped[create_at]

