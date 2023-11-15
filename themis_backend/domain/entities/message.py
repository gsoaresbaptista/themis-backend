from typing import NamedTuple
from uuid import UUID


class Message(NamedTuple):
    id: UUID
    user_id: UUID
    question: str
    answer: str
    create_at: str