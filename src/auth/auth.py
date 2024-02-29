import redis.asyncio
from fastapi_users.authentication import (
    AuthenticationBackend,
    RedisStrategy,
    # JWTStrategy,
    BearerTransport,

)
# from src.core.config import Settings

redis = redis.asyncio.from_url(
    "redis://localhost:6379",
    decode_responses=True,
)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


# def get_jwt_strategy() -> JWTStrategy:
#     return JWTStrategy(secret=Settings.SECRET, lifetime_seconds=3600)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=3600, key_prefix="movie")


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_redis_strategy,
)
