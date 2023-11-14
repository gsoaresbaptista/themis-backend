from starlette.applications import Starlette

from themis_backend.application.setup import (
    setup_exceptions,
    setup_routes,
    setup_startup,
)

app = Starlette(debug=True)

setup_routes(app)
setup_exceptions(app)
setup_startup(app)
