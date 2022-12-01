from faker import Faker
from src.data.test import RegisterUserSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import UserRepositorySpy
from .register_user_controller import RegisterUserController


faker = Faker()


def test_route():
    """Testing route method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)
    attributes = {"name": faker.word(), "password": faker.word()}

    response = register_user_route.route(HttpRequest(body=attributes))

    assert register_user_use_case.registry_param["name"] == attributes["name"]
    assert register_user_use_case.registry_param["password"] == attributes["password"]

    assert response.status_code == 200
    assert "error" not in response.body


def test_route_error_no_body():
    """Testing route method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)

    response = register_user_route.route(HttpRequest())

    assert register_user_use_case.registry_param == {}

    assert response.status_code == 400
    assert response.body == "Bad Request"


def test_route_error_wrong_body():
    """Testing route method in RegisterUserController"""

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_route = RegisterUserController(register_user_use_case)
    attributes = {
        "name": faker.random_number(digits=3),
        "password": faker.random_number(digits=3),
    }

    response = register_user_route.route(HttpRequest(body=attributes))

    assert register_user_use_case.registry_param["name"] == attributes["name"]
    assert register_user_use_case.registry_param["password"] == attributes["password"]

    assert response.status_code == 422
    assert response.body == "Unprocessable Entity"
