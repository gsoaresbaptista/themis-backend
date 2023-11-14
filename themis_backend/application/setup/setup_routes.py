from starlette.applications import Starlette

from themis_backend.application.routes import create_user_route


def setup_routes(app: Starlette) -> None:
    app.add_route('/users', create_user_route, methods=['POST'])
