from abc import ABC, abstractmethod
from typing import Optional

from themis_backend.domain.entities import User


class UserRepository(ABC):
    @abstractmethod
    async def create(
        self, name: str, email: str, hashed_password: str
    ) -> Optional[User]:
        ...

    @abstractmethod
    async def search_by_email(self, email: str) -> Optional[User]:
        ...
