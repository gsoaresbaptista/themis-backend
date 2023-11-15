from themis_backend.domain.repositories import UserRepository
from themis_backend.domain.services import AccessTokenService, HashService
from themis_backend.presentation.dtos import SignInDTO, UserViewDTO
from themis_backend.presentation.http.errors import (
    IncorrectPassword,
    UserNotFound,
)
from themis_backend.presentation.validators import SignInValidator


class SignIn:
    def __init__(
        self,
        repository: UserRepository,
        hash: HashService,
        token: AccessTokenService,
    ) -> None:
        self.__repository = repository
        self.__hash = hash
        self.__token = token

    async def execute(self, sign_in_dto: SignInDTO) -> str:
        validator = SignInValidator(sign_in_dto)
        validator.validate()

        user = await self.__repository.search_by_email(email=sign_in_dto.email)

        if not user:
            raise UserNotFound()

        if self.__hash.compare(sign_in_dto.password, user.hashed_password):
            return self.__token.create(UserViewDTO.from_user_dto(user))
        else:
            raise IncorrectPassword()
