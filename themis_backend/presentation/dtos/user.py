from typing import NamedTuple


class UserViewDTO(NamedTuple):
    id: str
    name: str
    email: str


class CreateUserDTO(NamedTuple):
    name: str
    email: str
    password: str


class UserDTO(NamedTuple):
    id: str
    name: str
    email: str
    hashed_password: str
