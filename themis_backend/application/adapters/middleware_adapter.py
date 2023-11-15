from starlette.requests import Request

from themis_backend.presentation.controllers import Controller
from themis_backend.presentation.http import HttpResponse


async def middleware_adapter(
    request: Request, controller: Controller
) -> HttpResponse:
    print(request.headers)
    return request
