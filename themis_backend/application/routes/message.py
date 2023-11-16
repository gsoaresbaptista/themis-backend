import asyncio

from starlette.background import BackgroundTask
from starlette.requests import Request
from starlette.responses import JSONResponse, Response, StreamingResponse

from themis_backend.application.adapters import request_adapter
from themis_backend.application.factories import (
    authenticate_composer,
    get_messages_compose,
)
from themis_backend.domain.services import BufferedGenerator
from themis_backend.domain.use_cases import CreateMessage
from themis_backend.external.repositories.postgre_message_repository import (
    PostgreMessageRepository,
)
from themis_backend.presentation.controllers import QuestionController
from themis_backend.presentation.dtos import CreateMessageDTO, TokenDTO


async def store_message(
    authorization: TokenDTO,
    question: str,
    generator: BufferedGenerator,
    lock: asyncio.Lock = None,
):
    if lock:
        lock.release()
    use_case = CreateMessage(repository=PostgreMessageRepository())
    await use_case.execute(
        CreateMessageDTO(
            user_id=authorization.user_id,
            question=question,
            answer=generator.get_text(),
        )
    )


async def question_route(request: Request) -> Response:
    response = await request_adapter(
        request, QuestionController(), middlewares=[authenticate_composer()]
    )

    question = response.body['data']['question']
    generator = request.app.model.generate(question)

    lock = request.app.model_lock
    if lock:
        await lock.acquire()

    task = BackgroundTask(
        store_message,
        generator=generator,
        question=question,
        authorization=response.authorization,
        lock=lock,
    )

    return StreamingResponse(
        generator,
        media_type='text/plain',
        background=task,
    )


async def get_messages(request: Request) -> Response:
    response = await request_adapter(
        request, get_messages_compose(), middlewares=[authenticate_composer()]
    )

    return JSONResponse(
        status_code=200,
        content=response.body,
    )
