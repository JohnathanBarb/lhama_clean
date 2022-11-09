from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser


faker = Faker()


def test_register():
    """Test registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.name(), "password": faker.name()}

    response = register_user.registry(
        name=attributes["name"], password=attributes["password"]
    )

    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    assert response["success"] is True
    assert response["data"]


def test_fail_register():
    """Test fail registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.random_number(), "password": faker.name()}

    response = register_user.registry(
        name=attributes["name"], password=attributes["password"]
    )

    assert not user_repo.insert_user_params

    assert response["success"] is False
    assert response["data"] is None
