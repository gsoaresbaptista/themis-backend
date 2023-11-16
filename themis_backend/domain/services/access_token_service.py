from abc import ABC, abstractmethod
from typing import Optional

from themis_backend.presentation.dtos import (
    AuthorizationHeaderDTO,
    TokenDTO,
    UserDTO,
)


class AccessTokenService(ABC):
    @abstractmethod
    def create(self, user: UserDTO) -> AuthorizationHeaderDTO:
        ...

    @abstractmethod
    def decode(self, token: str) -> Optional[TokenDTO]:
        ...
