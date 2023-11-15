from typing import Any, NamedTuple
from uuid import UUID


class User(NamedTuple):
    id: UUID
    name: str
    email: str
    hashed_password: str

    def _asdict(self, no_password: bool = True) -> dict[str, Any]:
        dict_user = {
            'id': self.id.hex,
            'name': self.name,
            'email': self.email,
        }

        if not no_password:
            dict_user.update()

        return dict_user
