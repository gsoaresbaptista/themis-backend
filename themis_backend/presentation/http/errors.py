from typing import Any


class HTTPError(Exception):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def to_dict(self) -> dict[str, Any]:
        return {'status_code': self.status_code, 'message': self.message}


class HTTPUnprocessableEntity(HTTPError):
    def __init__(self, errors: dict) -> None:
        super().__init__(
            422, 'Correct request structure, hindered by semantic errors.'
        )
        self.errors = errors

    def to_dict(self) -> dict[str, Any]:
        dict_data = super().to_dict()
        dict_data.update({'errors': self.errors})
        return dict_data


class UserAlreadyExists(HTTPError):
    def __init__(self, email: str) -> None:
        super().__init__(409, f'The email address {email} is already in use.')
        self.email = email

    def to_dict(self) -> dict[str, Any]:
        dict_data = super().to_dict()
        dict_data.update({'conflict_key': 'email', 'email': self.email})
        return dict_data
