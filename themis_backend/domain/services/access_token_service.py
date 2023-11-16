from abc import ABC, abstractmethod
from typing import Optional

from themis_backend.presentation.dtos import TokenDTO, UserDTO


class AccessTokenService(ABC):
    @abstractmethod
    def create(self, user: UserDTO) -> str:
        ...

    @abstractmethod
    def decode(self, token: str) -> Optional[TokenDTO]:
        ...
