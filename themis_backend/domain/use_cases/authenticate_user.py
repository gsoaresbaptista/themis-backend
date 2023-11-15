from typing import Optional

from themis_backend.domain.services import AccessTokenService
from themis_backend.presentation.dtos import UserViewDTO


class AuthenticateUser:
    def __init__(self, token_service: AccessTokenService) -> None:
        self.__token = token_service

    async def execute(self, bearer_token: str) -> Optional[UserViewDTO]:
        _, token = bearer_token.split(' ', 1)
        return self.__token.decode(token)
