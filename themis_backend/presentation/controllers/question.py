from themis_backend.presentation.http import (
    EmptyQuestionNotAllowed,
    HttpRequest,
    HttpResponse,
)

from .controller import Controller


class QuestionController(Controller):
    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        question = http_request.body.get('question', None)

        if question is None or question == '':
            raise EmptyQuestionNotAllowed()

        return question, http_request.authorization
