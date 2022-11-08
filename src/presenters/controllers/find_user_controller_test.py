from faker import Faker
from .find_user_controller import FindUserController
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_handle():
    """Testing Handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(
        query={"user_id": faker.random_number(), "user_name": faker.word()}
    )

    response = find_user_controller.handle(http_request)

    assert (
        find_user_use_case.by_id_and_name_param["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_param["name"]
        == http_request.query["user_name"]
    )

    assert response.status_code == 200
    assert response.body


def test_handle_query_user_id():
    """Testing Handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"user_id": faker.random_number()})

    response = find_user_controller.handle(http_request)

    assert find_user_use_case.by_id_param["user_id"] == http_request.query["user_id"]

    assert response.status_code == 200
    assert response.body


def test_handle_query_user_name():
    """Testing Handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"user_name": faker.word()})

    response = find_user_controller.handle(http_request)

    assert find_user_use_case.by_name_param["name"] == http_request.query["user_name"]

    assert response.status_code == 200
    assert response.body


def test_handle_no_query_param():
    """Testing Handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest()

    response = find_user_controller.handle(http_request)

    assert not find_user_use_case.by_id_and_name_param
    assert not find_user_use_case.by_id_param
    assert not find_user_use_case.by_name_param

    assert response.status_code == 400
    assert response.body == "Bad Request"
