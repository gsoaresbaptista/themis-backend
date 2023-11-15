from functools import wraps

from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response

from themis_backend.presentation.http.errors import HTTPUnauthorized


class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        request.state.authenticated_user = None
        response = await call_next(request)
        return response


def authenticated():
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            if request.state.authenticated_user is None:
                raise HTTPUnauthorized()
            return await func(request, *args, **kwargs)

        return wrapper

    return decorator
