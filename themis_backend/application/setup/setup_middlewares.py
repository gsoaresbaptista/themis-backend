from starlette.applications import Starlette

from themis_backend.application.middlewares import AuthenticationMiddleware


def setup_middlewares(app: Starlette) -> None:
    app.add_middleware(AuthenticationMiddleware)
