from themis_backend.domain.use_cases import RefreshToken
from themis_backend.presentation.http import HttpRequest, HttpResponse

from .controller import Controller


class RefreshTokenController(Controller):
    def __init__(self, use_case: RefreshToken) -> None:
        self.__use_case = use_case

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        refresh_token = http_request.body.get('refresh-token', None)
        access_token = await self.__use_case.execute(refresh_token)

        return HttpResponse(
            status_code=200,
            body={
                'data': {
                    'access_token': access_token,
                    'refresh_token': {'id': refresh_token},
                }
            },
        )
