from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import FindUser


faker = Faker()


def test_by_id():
    """testing by_id method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=4)}
    response = find_user.by_id(attributes["id"])

    assert user_repo.select_user_params["user_id"] == attributes["id"]

    assert response["success"] is True
    assert response["data"]


def test_fail_by_id():
    """testing by_id method failing"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.name()}
    response = find_user.by_id(attributes["id"])

    assert not user_repo.select_user_params

    assert response["success"] is False
    assert response["data"] is None


def test_by_name():
    """testing by_name method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.name()}
    response = find_user.by_name(attributes["name"])

    assert user_repo.select_user_params["name"] == attributes["name"]

    assert response["success"] is True
    assert response["data"]


def test_fail_by_name():
    """testing by_name method failing"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.random_number(digits=4)}
    response = find_user.by_name(attributes["name"])

    assert not user_repo.select_user_params

    assert response["success"] is False
    assert response["data"] is None


def test_by_id_and_name():
    """testing by_id_and_name method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.name(), "id": faker.random_number(digits=4)}
    response = find_user.by_id_and_name(attributes["id"], attributes["name"])

    assert user_repo.select_user_params["user_id"] == attributes["id"]
    assert user_repo.select_user_params["name"] == attributes["name"]

    assert response["success"] is True
    assert response["data"]


def test_by_id_and_name_fail_by_name():
    """testing by_id_and_name method failing"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.random_number(digits=4), "id": faker.random_number()}
    response = find_user.by_id_and_name(attributes["id"], attributes["name"])

    assert not user_repo.select_user_params

    assert response["success"] is False
    assert not response["data"]


def test_by_id_and_name_fail_by_user_id():
    """testing by_id_and_name method failing"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.name(), "id": faker.name()}
    response = find_user.by_id_and_name(attributes["id"], attributes["name"])

    assert not user_repo.select_user_params

    assert response["success"] is False
    assert not response["data"]
