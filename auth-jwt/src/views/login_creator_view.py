from typing import Any, cast

from src.controllers.interfaces.login_creator import LoginCreatorInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from .interfaces.view_interface import ViewInterface


class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body or {}
        username = body.get("username")
        password = body.get("password")
        self.__validate_inputs(username, password)

        response = self.__controller.create(cast(str, username), cast(str, password))
        return HttpResponse(body={"data": response}, status_code=200)

    def __validate_inputs(self, username: Any, password: Any) -> None:
        if (
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ):
            raise HttpBadRequestError("Invalid Input")
