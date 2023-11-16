from typing import NamedTuple
from uuid import UUID


class CreateMessageDTO(NamedTuple):
    user_id: UUID
    question: str
    answer: str
