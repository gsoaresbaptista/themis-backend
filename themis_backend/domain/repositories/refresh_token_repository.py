from abc import ABC, abstractmethod
from typing import Optional

from themis_backend.domain.entities import RefreshToken


class RefreshTokenRepository(ABC):
    @abstractmethod
    async def create(self, user_id: str) -> Optional[RefreshToken]:
        ...

    @abstractmethod
    async def search_by_user_id(self, user_id: str) -> Optional[RefreshToken]:
        ...
