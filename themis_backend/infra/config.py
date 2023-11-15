from typing import NamedTuple

from dotenv import dotenv_values

env_file = dotenv_values('.env')


class DatabaseSettings(NamedTuple):
    DATABASE_USER: str = env_file.get('DATABASE_USER')
    DATABASE_PASSWORD: str = env_file.get('DATABASE_PASSWORD')
    DATABASE_HOST: str = env_file.get('DATABASE_HOST')
    DATABASE_PORT: int = env_file.get('DATABASE_PORT')
    DATABASE_NAME: str = env_file.get('DATABASE_NAME')


class TokenSettings(NamedTuple):
    ALGORITHM: str = env_file.get('ALGORITHM')
    SECRET_KEY: str = env_file.get('SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        env_file.get('ACCESS_TOKEN_EXPIRE_MINUTES')
    )
