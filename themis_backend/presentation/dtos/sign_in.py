from typing import NamedTuple


class SignInDTO(NamedTuple):
    email: str
    password: str
