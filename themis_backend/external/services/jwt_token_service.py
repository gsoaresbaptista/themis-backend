from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt

from themis_backend.config import TokenSettings
from themis_backend.domain.services import AccessTokenService
from themis_backend.presentation.dtos import TokenDTO, UserViewDTO


class JTWAccessTokenService(AccessTokenService):
    def __init__(self) -> None:
        self.__expire_minutes = TokenSettings.EXPIRE_MINUTES
        self.__algorithm = TokenSettings.ALGORITHM
        self.__secret_key = TokenSettings.SECRET_KEY

    def create(self, user: UserViewDTO) -> str:

        data = user._asdict()
        expire = datetime.utcnow() + timedelta(minutes=self.__expire_minutes)
        data.update({'exp': expire})
        encoded_jwt = jwt.encode(
            data, self.__secret_key, algorithm=self.__algorithm
        )

        return encoded_jwt

    def decode(self, token: str) -> Optional[TokenDTO]:
        try:
            payload = jwt.decode(
                token, key=self.__secret_key, algorithms=self.__algorithm
            )
            return TokenDTO(
                user_id=payload['id'],
                name=payload['name'],
                email=payload['email'],
            )
        except JWTError:
            return None
