from starlette.applications import Starlette

from themis_backend.application.routes import (
    clear_chat,
    continue_answer,
    create_user_route,
    delete_message,
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
    app.add_route('/messages', get_messages, methods=['GET'])
    app.add_route('/messages/clear-chat', clear_chat, methods=['DELETE'])
    app.add_route('/messages/continue', continue_answer, methods=['POST'])
    app.add_route(
        '/messages/{message_id:str}', delete_message, methods=['DELETE']
    )
