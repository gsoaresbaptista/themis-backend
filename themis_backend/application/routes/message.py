import asyncio

from starlette.background import BackgroundTask
from starlette.requests import Request
from starlette.responses import JSONResponse, Response, StreamingResponse

from themis_backend.application.adapters import request_adapter
from themis_backend.application.factories import (
    authenticate_composer,
    clear_chat_compose,
    continue_answer_compose,
    delete_message_compose,
    get_messages_compose,
)
from themis_backend.domain.services import BufferedGenerator
from themis_backend.domain.use_cases import CreateMessage, UpdateMessageAnswer
from themis_backend.external.repositories.postgre_message_repository import (
    PostgreMessageRepository,
)
from themis_backend.presentation.controllers import QuestionController
from themis_backend.presentation.dtos import (
    CreateMessageDTO,
    TokenDTO,
    UpdateMessageAnswerDTO,
)


async def store_message(
    authorization: TokenDTO,
    question: str,
    answer: BufferedGenerator,
    lock: asyncio.Lock = None,
):
    if lock:
        lock.release()
    use_case = CreateMessage(repository=PostgreMessageRepository())
    await use_case.execute(
        CreateMessageDTO(
            user_id=authorization.user_id,
            question=question,
            answer=answer.get_text(),
        )
    )


async def update_message_answer(
    authorization: TokenDTO,
    message_id: int,
    answer: (str, BufferedGenerator),
    lock: asyncio.Lock = None,
):
    if lock:
        lock.release()
    use_case = UpdateMessageAnswer(repository=PostgreMessageRepository())
    await use_case.execute(
        UpdateMessageAnswerDTO(
            user_id=authorization.user_id,
            message_id=message_id,
            answer=answer[0] + answer[1].get_text(),
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
        answer=generator,
        question=question,
        authorization=response.authorization,
        lock=lock,
    )

    return StreamingResponse(
        generator,
        media_type='text/plain',
        background=task,
    )


async def continue_answer(request: Request) -> Response:
    response = await request_adapter(
        request,
        continue_answer_compose(),
        middlewares=[authenticate_composer()],
    )

    message = response.body['data']['message']
    previous_answer = message.answer[-512:]
    generator = request.app.model.generate(previous_answer)

    lock = request.app.model_lock
    if lock:
        await lock.acquire()

    task = BackgroundTask(
        update_message_answer,
        message_id=message.id,
        answer=(previous_answer, generator),
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
        status_code=response.status_code,
        content=response.body,
    )


async def delete_message(request: Request) -> Response:
    response = await request_adapter(
        request,
        delete_message_compose(),
        middlewares=[authenticate_composer()],
    )

    return JSONResponse(
        status_code=response.status_code,
        content=response.body,
    )


async def clear_chat(request: Request) -> Response:
    response = await request_adapter(
        request,
        clear_chat_compose(),
        middlewares=[authenticate_composer()],
    )

    return JSONResponse(
        status_code=response.status_code,
        content=response.body,
    )
