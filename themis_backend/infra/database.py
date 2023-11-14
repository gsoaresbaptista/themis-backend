from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from themis_backend.infra.config import DatabaseSettings
from themis_backend.infra.schemas import BaseSchema, UserSchema  # noqa: F401


async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(BaseSchema.metadata.create_all)


db_settings = DatabaseSettings()

engine = create_async_engine(
    'postgresql+asyncpg://{}:{}@{}:{}/{}'.format(
        db_settings.DATABASE_USER,
        db_settings.DATABASE_PASSWORD,
        db_settings.DATABASE_HOST,
        db_settings.DATABASE_PORT,
        db_settings.DATABASE_NAME,
    ),
)


Session = async_sessionmaker(engine, expire_on_commit=False)
