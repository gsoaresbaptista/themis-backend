from starlette.applications import Starlette

from themis_backend.application.routes import (
    create_user_route,
    get_messages,
    question_route,
    refresh_token_route,
    sign_in_route,
)


# TODO: add openapi and an interface
def setup_routes(app: Starlette) -> None:
    app.add_route('/users/sign-up', create_user_route, methods=['POST'])
    app.add_route('/users/sign-in', sign_in_route, methods=['POST'])
    app.add_route(
        '/users/refresh-token', refresh_token_route, methods=['POST']
    )
    app.add_route('/messages/question', question_route, methods=['POST'])
    app.add_route('/messages/', get_messages, methods=['GET'])
