from starlette.requests import Request
from starlette.responses import Response, StreamingResponse


async def question_route(request: Request) -> Response:
    question = (await request.json()).get('question')

    return StreamingResponse(
        request.app.model(question, stream=True), media_type='text/plain'
    )
