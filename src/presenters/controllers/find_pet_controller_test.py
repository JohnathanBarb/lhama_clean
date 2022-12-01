from faker import Faker
from src.data.test import FindPetSpy
from src.infra.test import PetRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_pet_controller import FindPetController

faker = Faker()


def test_route():
    """Testing route method in FindPetController"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_router = FindPetController(find_pet_use_case)
    attributes = {
        "pet_id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=3),
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_router.route(http_request)

    assert (
        find_pet_use_case.by_pet_id_and_user_id_params["pet_id"] == attributes["pet_id"]
    )
    assert (
        find_pet_use_case.by_pet_id_and_user_id_params["user_id"]
        == attributes["user_id"]
    )

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_by_pet_id():
    """Testing route method in FindPetController"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_router = FindPetController(find_pet_use_case)
    attributes = {
        "pet_id": faker.random_number(digits=2),
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_router.route(http_request)

    assert find_pet_use_case.by_pet_id_params["pet_id"] == attributes["pet_id"]

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_by_user_id():
    """Testing route method in FindPetController"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_router = FindPetController(find_pet_use_case)
    attributes = {
        "user_id": faker.random_number(digits=3),
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_router.route(http_request)

    assert find_pet_use_case.by_user_id_params["user_id"] == attributes["user_id"]

    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_no_query():
    """Testing route method in FindPetController"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_router = FindPetController(find_pet_use_case)

    http_request = HttpRequest()

    http_response = find_pet_router.route(http_request)

    assert find_pet_use_case.by_pet_id_and_user_id_params == {}
    assert find_pet_use_case.by_pet_id_params == {}
    assert find_pet_use_case.by_user_id_params == {}

    assert http_response.status_code == 400
    assert http_response.body == "Bad Request"


def test_route_wrong_query():
    """Testing route method in FindPetController"""

    find_pet_use_case = FindPetSpy(PetRepositorySpy())
    find_pet_router = FindPetController(find_pet_use_case)
    attributes = {
        "pet_id": faker.word(),
        "user_id": faker.word(),
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_pet_router.route(http_request)

    assert (
        find_pet_use_case.by_pet_id_and_user_id_params["pet_id"] == attributes["pet_id"]
    )
    assert (
        find_pet_use_case.by_pet_id_and_user_id_params["user_id"]
        == attributes["user_id"]
    )

    assert http_response.status_code == 422
    assert http_response.body == "Unprocessable Entity"
