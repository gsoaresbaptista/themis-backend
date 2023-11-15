from __future__ import annotations

from typing import NamedTuple


class UserViewDTO(NamedTuple):
    id: str
    name: str
    email: str

    @staticmethod
    def from_user_dto(user: UserDTO) -> UserViewDTO:
        return UserViewDTO(id=user.id.hex, name=user.name, email=user.email)


class CreateUserDTO(NamedTuple):
    name: str
    email: str
    password: str


class UserDTO(NamedTuple):
    id: str
    name: str
    email: str
    hashed_password: str
