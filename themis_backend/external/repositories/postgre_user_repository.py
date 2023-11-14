from typing import Optional

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from themis_backend.domain.entities import User
from themis_backend.domain.repositories import UserRepository
from themis_backend.infra.database import Session
from themis_backend.infra.schemas import UserSchema
from themis_backend.presentation.http import UserAlreadyExists


class PostgreUserRepository(UserRepository):
    async def create(
        self, name: str, email: str, hashed_password: bytes
    ) -> Optional[User]:

        user = UserSchema(
            name=name,
            email=email,
            hashed_password=hashed_password,
        )

        try:
            async with Session() as session:
                session.add(user)
                await session.commit()
                await session.refresh(user)
        except IntegrityError as exception:
            if 'violates unique constraint' in str(exception.orig):
                raise UserAlreadyExists(email=email) from exception
            raise

        return user

        #     async with Session() as session:
        #         query = select(UserSchema).where(UserSchema.email == email)
        #         user = await session.execute(query)
        #     raise
        # finally:
        #     return user.scalar()

    async def search_by_email(self, email: str) -> Optional[User]:
        async with Session() as session:
            query = select(UserSchema).where(UserSchema.email == email)
            user = await session.execute(query)

        return user.scalar()
