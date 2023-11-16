from datetime import datetime
from typing import Any, NamedTuple
from uuid import UUID


class RefreshToken(NamedTuple):
    id: UUID
    user_id: UUID
    expires_in: datetime

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id.hex,
            'user_id': self.user_id,
            'expires_in': self.created_at.strftime('%Y-%m-%d, %H:%M:%S'),
        }
