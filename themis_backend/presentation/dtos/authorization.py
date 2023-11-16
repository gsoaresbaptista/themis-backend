from typing import NamedTuple


class TokenDTO(NamedTuple):
    user_id: str
    name: str
    email: str


class AuthorizationHeaderDTO(NamedTuple):
    access_token: str
    refresh_token: dict[str, str]
