import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Uuid, func
from sqlalchemy.orm import MappedColumn, mapped_column

from themis_backend.infra.schemas.base import BaseSchema


class RefreshTokenSchema(BaseSchema):
    __tablename__ = 'refresh_tokens'

    id: MappedColumn[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, default=uuid.uuid4
    )
    user_id: MappedColumn[uuid.UUID] = mapped_column(ForeignKey('users.id'))
    expires_in: MappedColumn[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )

    def __repr__(self):
        return f'<RefreshToken (user_id={self.user_id}, expiresIn={self.expires_in}>'
