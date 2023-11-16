from datetime import datetime

from themis_backend.domain.entities import RefreshToken
from themis_backend.domain.repositories import (
    RefreshTokenRepository,
    UserRepository,
)
from themis_backend.domain.services import AccessTokenService, HashService
from themis_backend.presentation.dtos import AuthorizationHeaderDTO, SignInDTO
from themis_backend.presentation.http.errors import (
    IncorrectPassword,
    UserNotFound,
)
from themis_backend.presentation.validators import SignInValidator


class SignIn:
    def __init__(
        self,
        repository: UserRepository,
        hash_service: HashService,
        token_service: AccessTokenService,
        refresh_token_repository: RefreshTokenRepository,
    ) -> None:
        self.__user_repository = repository
        self.__hash = hash_service
        self.__token = token_service
        self.__refresh_token_repository = refresh_token_repository

    async def execute(self, sign_in_dto: SignInDTO) -> AuthorizationHeaderDTO:
        validator = SignInValidator(sign_in_dto)
        validator.validate()

        user = await self.__user_repository.search_by_email(
            email=sign_in_dto.email
        )

        if not user:
            raise UserNotFound()

        if self.__hash.compare(sign_in_dto.password, user.hashed_password):
            access_token = self.__token.create(user)

            refresh_token = (
                await self.__refresh_token_repository.search_by_user_id(
                    user.id
                )
            )

            expires_in = refresh_token.expires_in
            now = datetime.now(refresh_token.expires_in.tzinfo)

            if refresh_token is None or expires_in < now:
                await self.__refresh_token_repository.delete_all(
                    user_id=user.id
                )
                refresh_token = await self.__refresh_token_repository.create(
                    user_id=user.id
                )

            refresh_token = RefreshToken(
                id=refresh_token.id,
                user_id=refresh_token.id,
                expires_in=refresh_token.expires_in,
            )

            return AuthorizationHeaderDTO(
                access_token=access_token,
                refresh_token=refresh_token.to_dict(),
            )
        else:
            raise IncorrectPassword()
