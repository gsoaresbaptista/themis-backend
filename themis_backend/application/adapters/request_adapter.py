from json import JSONDecodeError

from starlette.requests import Request

from themis_backend.presentation.controllers import Controller
from themis_backend.presentation.http import HttpRequest, HttpResponse
from themis_backend.presentation.http.errors import HTTPBadRequest


async def request_adapter(
    request: Request, controller: Controller
) -> HttpResponse:
    body = {}

    if request.method != 'GET':
        try:
            body = await request.json()
        except JSONDecodeError:
            raise HTTPBadRequest()

    http_request = HttpRequest(body=body)
    http_response = await controller.handle(http_request)

    return http_response
