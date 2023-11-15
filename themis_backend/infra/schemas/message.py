import uuid
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import MappedColumn, mapped_column
from sqlalchemy.types import DATE, String, Uuid

from themis_backend.infra.schemas.base import BaseSchema


class MessageSchema(BaseSchema):
    __tablename__ = 'messages'

    id: MappedColumn[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, default=uuid.uuid4
    )
    user_id: MappedColumn[uuid.UUID] = mapped_column(ForeignKey('users.id'))
    question: MappedColumn[str] = mapped_column(String)
    answer: MappedColumn[str] = mapped_column(String)
    create_at: MappedColumn[datetime] = mapped_column(
        DATE, default=datetime.now()
    )

    def __repr__(self):
        return (
            f'<MessageSchema (question={self.question}, answer={self.answer}>'
        )
