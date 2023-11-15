from datetime import datetime, timedelta

from jose import jwt

from themis_backend.domain.services import AccessTokenService
from themis_backend.infra import TokenSettings
from themis_backend.presentation.dtos import UserViewDTO


class JTWAccessTokenService(AccessTokenService):
    def create(self, user: UserViewDTO) -> str:
        token_settings = TokenSettings()
        expire_minutes = token_settings.ACCESS_TOKEN_EXPIRE_MINUTES
        algorithm = token_settings.ALGORITHM
        secret_key = token_settings.SECRET_KEY

        data = user._asdict()
        expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
        data.update({'exp': expire})
        encoded_jwt = jwt.encode(data, secret_key, algorithm=algorithm)

        return encoded_jwt
