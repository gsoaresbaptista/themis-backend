from themis_backend.domain.use_cases import ContinueAnswer
from themis_backend.presentation.dtos import ContinueAnswerDTO
from themis_backend.presentation.http import HttpRequest, HttpResponse

from .controller import Controller


class ContinueAnswerController(Controller):
    def __init__(self, use_case: ContinueAnswer) -> None:
        self.__use_case = use_case

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        continue_dto = ContinueAnswerDTO(
            message_id=http_request.body.get('message-id', None)
        )

        message = await self.__use_case.execute(continue_dto)

        return HttpResponse(
            status_code=200,
            body={'data': {'message': message}},
            authorization=http_request.authorization,
        )
