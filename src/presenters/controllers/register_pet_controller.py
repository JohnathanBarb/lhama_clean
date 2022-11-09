from typing import Type

from src.presenters.helpers import HttpRequest, HttpResponse
from src.domain.use_cases import RegisterPet
from src.presenters.errors import HttpErrors


class RegisterPetController:
    """Class to define route to RegisterPet use case"""

    def __init__(self, register_pet_use_case: Type[RegisterPet]):
        self.register_pet_use_case = register_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:

            body_param = http_request.body.keys()

            if (
                "name" in body_param
                and "specie" in body_param
                and "user_information" in body_param
            ):

                user_information_params = http_request.body["user_information"]

                if (
                    "user_id" in user_information_params
                    or "user_name" in user_information_params
                ):
                    name = http_request.body["name"]
                    specie = http_request.body["specie"]
                    user_information = http_request.body["user_information"]

                    age = http_request.body.get("age", None)

                    response = self.register_pet_use_case.registry(
                        name=name,
                        specie=specie,
                        user_information=user_information,
                        age=age,
                    )

                else:
                    response = {"success": False, "data": None}
            else:
                response = {"success": False, "data": None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
