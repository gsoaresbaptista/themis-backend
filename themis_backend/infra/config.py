from typing import NamedTuple

from dotenv import dotenv_values

env_file = dotenv_values('.env')


class DatabaseSettings(NamedTuple):
    DATABASE_USER: str = env_file.get('DATABASE_USER')
    DATABASE_PASSWORD: str = env_file.get('DATABASE_PASSWORD')
    DATABASE_HOST: str = env_file.get('DATABASE_HOST')
    DATABASE_PORT: int = env_file.get('DATABASE_PORT')
    DATABASE_NAME: str = env_file.get('DATABASE_NAME')
