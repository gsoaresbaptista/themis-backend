import asyncio

from starlette.background import BackgroundTask
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse

from themis_backend.application.adapters import request_adapter
from themis_backend.application.factories import authenticate_composer
from themis_backend.domain.services import BufferedGenerator
from themis_backend.external.repositories.postgre_message_repository import (
    PostgreMessageRepository,
)
from themis_backend.presentation.controllers import QuestionController
from themis_backend.presentation.dtos import UserViewDTO


async def store_message(
    user_view: UserViewDTO,
    question: str,
    generator: BufferedGenerator,
    lock: asyncio.Lock = None,
):
    if lock:
        lock.release()

    repository = PostgreMessageRepository()

    await repository.create(
        user_id=user_view.user_id,
        question=question,
        answer=generator.get_text(),
    )


async def question_route(request: Request) -> Response:
    response = await request_adapter(
        request, QuestionController(), middlewares=[authenticate_composer()]
    )

    question = response.body['data']['question']

    lock = request.app.model_lock
    generator = request.app.model.generate(question)
    if lock:
        await lock.acquire()

    task = BackgroundTask(
        store_message,
        generator=generator,
        question=question,
        user_view=response.authorization,
        lock=lock,
    )

    return StreamingResponse(
        generator,
        media_type='text/plain',
        background=task,
    )
