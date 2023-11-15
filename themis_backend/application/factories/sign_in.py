from themis_backend.domain.use_cases import SignIn
from themis_backend.external.repositories import PostgreUserRepository
from themis_backend.external.services import (
    BcryptHashService,
    JTWAccessTokenService,
)
from themis_backend.presentation.controllers import (
    Controller,
    SignInController,
)


def sign_in_composer() -> Controller:
    repository = PostgreUserRepository()
    hash_service = BcryptHashService()
    token_service = JTWAccessTokenService()
    use_case = SignIn(repository, hash_service, token_service)
    controller = SignInController(use_case)
    return controller
