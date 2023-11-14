from typing import NamedTuple
from uuid import UUID


class User(NamedTuple):
    id: UUID
    name: str
    email: str
    hashed_password: str
