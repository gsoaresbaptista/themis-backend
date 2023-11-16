from typing import Optional
from uuid import UUID

from sqlalchemy import select

from themis_backend.domain.entities import Message
from themis_backend.domain.repositories import MessageRepository
from themis_backend.infra.database import Session
from themis_backend.infra.schemas import MessageSchema


def user_row_to_entity(row: MessageSchema) -> Message:
    return Message(
        id=row.id,
        user_id=row.user_id,
        question=row.question,
        answer=row.answer,
        created_at=row.created_at,
    )


class PostgreMessageRepository(MessageRepository):
    async def create(
        self, user_id: UUID, question: str, answer: str
    ) -> Optional[Message]:

        message = MessageSchema(
            user_id=user_id,
            question=question,
            answer=answer,
        )

        async with Session() as session:
            session.add(message)
            await session.commit()
            await session.refresh(message)

        return user_row_to_entity(message)

    async def search_by_user_id(self, user_id: UUID) -> list[Message]:
        async with Session() as session:
            query = select(MessageSchema).where(
                MessageSchema.user_id == user_id
            )
            messages = await session.execute(query)

        return [user_row_to_entity(message) for message in messages]
