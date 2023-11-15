from abc import ABC, abstractmethod
from typing import Optional

from themis_backend.presentation.dtos import TokenDTO, UserViewDTO


class AccessTokenService(ABC):
    @abstractmethod
    def create(self, user: UserViewDTO) -> str:
        ...

    @abstractmethod
    def decode(self, token: str) -> Optional[TokenDTO]:
        ...
