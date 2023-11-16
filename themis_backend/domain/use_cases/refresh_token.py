from datetime import datetime
from uuid import UUID

from themis_backend.domain.entities import User
from themis_backend.domain.repositories import (
    RefreshTokenRepository,
    UserRepository,
)
from themis_backend.domain.services import AccessTokenService
from themis_backend.presentation.dtos import AuthorizationHeaderDTO
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

    async def execute(
        self, refresh_token_id: UUID | str
    ) -> AuthorizationHeaderDTO:
        try:
            refresh_token = await self.__refresh_token_repository.search_by_id(
                refresh_token_id
            )
        except:   # noqa: E722
            raise HTTPUnauthorized()

        if refresh_token is not None:
            expires_in = refresh_token.expires_in
            now = datetime.now(refresh_token.expires_in.tzinfo)

            if expires_in > now:
                user = await self.__user_repository.search_by_id(
                    refresh_token.user_id
                )
                if user is not None:
                    access_token = self.__token_service.create(
                        User(
                            id=user.id,
                            name=user.name,
                            email=user.email,
                            hashed_password=user.hashed_password,
                            created_at=user.created_at,
                            updated_at=user.updated_at,
                        )
                    )
                    await self.__refresh_token_repository.delete_all(
                        user_id=user.id
                    )
                    refresh_token = (
                        await self.__refresh_token_repository.create(
                            user_id=user.id
                        )
                    )
                    return AuthorizationHeaderDTO(
                        access_token=access_token,
                        refresh_token=refresh_token.to_dict(),
                    )

        raise HTTPUnauthorized()
