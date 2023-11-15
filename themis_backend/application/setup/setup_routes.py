from starlette.applications import Starlette

from themis_backend.application.routes import create_user_route, sign_in_route


# TODO: add openapi and an interface
def setup_routes(app: Starlette) -> None:
    app.add_route('/users', create_user_route, methods=['POST'])
    app.add_route('/sign-in', sign_in_route, methods=['POST'])
