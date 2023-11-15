from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from themis_backend.domain.entities import Message


class MessageRepository(ABC):
    @abstractmethod
    async def create(
        self, user_id: UUID, question: str, answer: str
    ) -> Optional[Message]:
        ...

    @abstractmethod
    async def search_by_user_id(self, user_id: UUID) -> list[Message]:
        ...
