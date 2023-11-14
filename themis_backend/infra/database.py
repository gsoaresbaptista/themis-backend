import asyncio

from dotenv import dotenv_values
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from themis_backend.infra.schemas import BaseSchema, UserSchema  # noqa: F401


async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(BaseSchema.metadata.create_all)


env_file = dotenv_values('.env')

engine = create_async_engine(
    'postgresql+asyncpg://{}:{}@{}:{}/{}'.format(
        env_file.get('DATABASE_USER'),
        env_file.get('DATABASE_PASSWORD'),
        env_file.get('DATABASE_HOST'),
        env_file.get('DATABASE_PORT'),
        env_file.get('DATABASE_NAME'),
    ),
)


Session = async_sessionmaker(engine, expire_on_commit=False)
