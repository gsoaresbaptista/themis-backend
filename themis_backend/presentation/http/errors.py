from typing import Any


class HTTPError(Exception):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def to_dict(self) -> dict[str, Any]:
        return {'status_code': self.status_code, 'message': self.message}


class UserAlreadyExists(HTTPError):
    def __init__(self, email: str) -> None:
        super().__init__(409, f'The email address {email} is already in use.')
        self.email = email

    def to_dict(self) -> dict[str, Any]:
        dict_data = super().to_dict()
        dict_data.update({'conflict_key': 'email', 'email': self.email})
        return dict_data
