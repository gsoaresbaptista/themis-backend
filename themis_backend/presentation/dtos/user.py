from __future__ import annotations

from typing import NamedTuple
from datetime import datetime


class UserViewDTO(NamedTuple):
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_user_dto(user: UserDTO) -> UserViewDTO:
        return UserViewDTO(id=user.id, name=user.name, email=user.email)


class CreateUserDTO(NamedTuple):
    name: str
    email: str
    password: str


class UserDTO(NamedTuple):
    id: str
    name: str
    email: str
    hashed_password: str
    created_at: datetime
    updated_at: datetime


class SignInDTO(NamedTuple):
    email: str
    password: str
