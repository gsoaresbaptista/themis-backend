from typing import NamedTuple
from uuid import UUID


class Message(NamedTuple):
    id: UUID
    user_id: UUID
    question: str
    answer: str
    created_at: str

    def to_dict(self) -> dict[str, str]:
        return {
            'question': self.question,
            'answer': self.answer,
            'created_at': self.created_at.strftime('%Y-%m-%d, %H:%M:%S'),
        }
