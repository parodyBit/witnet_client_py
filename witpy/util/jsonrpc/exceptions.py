from .response import ErrorResponse


class JsonRpcClientError(Exception):
    """Base class for the other exceptions."""

    pass


class ReceivedNon2xxResponseError(JsonRpcClientError):
    """The response was not valid JSON."""

    def __init__(self, status_code: int) -> None:
        super().__init__("Received {} status code".format(status_code))
        self.code = status_code


class ReceivedErrorResponseError(JsonRpcClientError):
    """The response was an error response."""

    def __init__(self, response: ErrorResponse) -> None:
        super().__init__(response.message)
        self.response = response
