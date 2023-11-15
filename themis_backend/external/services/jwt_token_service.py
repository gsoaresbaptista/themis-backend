from datetime import datetime, timedelta

from jose import jwt

from themis_backend.config import TokenSettings
from themis_backend.domain.services import AccessTokenService
from themis_backend.presentation.dtos import UserViewDTO


class JTWAccessTokenService(AccessTokenService):
    def create(self, user: UserViewDTO) -> str:
        expire_minutes = TokenSettings.ACCESS_TOKEN_EXPIRE_MINUTES
        algorithm = TokenSettings.ALGORITHM
        secret_key = TokenSettings.SECRET_KEY

        data = user._asdict()
        expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
        data.update({'exp': expire})
        encoded_jwt = jwt.encode(data, secret_key, algorithm=algorithm)

        return encoded_jwt
