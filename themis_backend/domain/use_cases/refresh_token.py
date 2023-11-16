from datetime import datetime
from uuid import UUID

from themis_backend.domain.repositories import (
    RefreshTokenRepository,
    UserRepository,
)
from themis_backend.domain.services import AccessTokenService
from themis_backend.presentation.dtos import UserDTO
from themis_backend.presentation.http.errors import HTTPUnauthorized


class RefreshToken:
    def __init__(
        self,
        refresh_token_repository: RefreshTokenRepository,
        user_repository: UserRepository,
        token_service: AccessTokenService,
    ) -> None:
        self.__refresh_token_repository = refresh_token_repository
        self.__user_repository = user_repository
        self.__token_service = token_service

    async def execute(self, refresh_token_id: UUID) -> str:
        refresh_token = await self.__repository.search_by_id(refresh_token_id)

        if refresh_token is not None:
            expires_in = refresh_token.expires_in
            now = datetime.now(refresh_token.expires_in.tzinfo)

            if expires_in > now:
                user = await self.__user_repository.search_by_id(
                    refresh_token.user_id
                )

                return self.__token_service.create(
                    UserDTO(
                        id=user.id,
                        name=user.name,
                        email=user.email,
                        hashed_password=user.hashed_password,
                        created_at=user.created_at,
                        updated_at=user.updated_at,
                    )
                )

        raise HTTPUnauthorized()
