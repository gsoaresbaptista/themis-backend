from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from themis_backend.domain.use_cases import CreateUser
from themis_backend.external.repositories import PostgreUserRepository
from themis_backend.external.services import BcryptHashService
from themis_backend.presentation.dtos import CreateUserDTO


async def create_user_route(request: Request) -> Response:
    repository = PostgreUserRepository()
    hash_service = BcryptHashService()
    use_case = CreateUser(repository, hash_service)

    body = await request.json()
    dto = CreateUserDTO(
        name=body['name'], email=body['email'], password=body['password']
    )

    user = await use_case.execute(dto)

    return JSONResponse(
        status_code=201,
        content={
            'user': {'id': user.id.hex, 'email': user.email, 'name': user.name}
        },
    )
