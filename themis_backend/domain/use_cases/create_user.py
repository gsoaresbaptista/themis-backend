from typing import Optional

from themis_backend.domain.entities import User
from themis_backend.domain.repositories import UserRepository
from themis_backend.domain.services import HashService


class CreateUser:
    def __init__(
        self, repository: UserRepository, hash: HashService
    ) -> Optional[User]:
        self.__repository = repository
        self.__hash = hash

    async def execute(
        self, name: str, email: str, password: str
    ) -> Optional[User]:
        user = await self.__repository.create(
            name=name, email=email, hashed_password=self.__hash.hash(password)
        )
        return user
