from typing import NamedTuple


class CreateMessageDTO(NamedTuple):
    user_id: str
    question: str
    answer: str
