from starlette.requests import Request

from themis_backend.presentation.controllers import Controller
from themis_backend.presentation.http import HttpRequest, HttpResponse


async def request_adapter(
    request: Request, controller: Controller
) -> HttpResponse:
    body = await request.json()

    http_request = HttpRequest(body=body)
    http_response = await controller.handle(http_request)

    return http_response
