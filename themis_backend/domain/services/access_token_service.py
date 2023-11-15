from abc import ABC, abstractmethod

from themis_backend.presentation.dtos import UserViewDTO


class AccessTokenService(ABC):
    @abstractmethod
    def create(self, user: UserViewDTO) -> str:
        ...
