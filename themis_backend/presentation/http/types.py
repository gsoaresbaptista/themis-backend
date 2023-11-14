from typing import Any, NamedTuple, Optional


class HttpRequest(NamedTuple):
    body: Optional[Any]


class HttpResponse(NamedTuple):
    status_code: int
    body: Any
