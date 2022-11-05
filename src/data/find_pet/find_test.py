from faker import Faker
from src.infra.test import PetRepositorySpy
from .find import FindPet


faker = Faker()


def test_by_pet_id():
    """testing by_pet_id method"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.random_number(digits=2)}
    response = find_pet.by_pet_id(attributes["pet_id"])

    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]

    assert response["success"] is True
    assert response["data"]


def test_by_pet_id_failing():
    """testing by_pet_id method failing"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.name()}
    response = find_pet.by_pet_id(attributes["pet_id"])

    assert not pet_repo.select_pet_params

    assert response["success"] is False
    assert not response["data"]


def test_by_user_id():
    """testing by_user_id method"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.random_number(digits=2)}
    response = find_pet.by_user_id(attributes["user_id"])

    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    assert response["success"] is True
    assert response["data"]


def test_by_user_id_failing():
    """testing by_user_id method failing"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.name()}
    response = find_pet.by_user_id(attributes["user_id"])

    assert not pet_repo.select_pet_params

    assert response["success"] is False
    assert not response["data"]


def test_by_pet_id_and_user_id():
    """testing by_pet_id_and_user_id method"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {
        "pet_id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }
    response = find_pet.by_pet_id_and_user_id(
        attributes["pet_id"], attributes["user_id"]
    )

    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]
    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    assert response["success"] is True
    assert response["data"]


def test_by_pet_id_and_user_id_failing_by_pet_id():
    """testing by_pet_id_and_user_id method failing by pet_id"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.name(), "user_id": faker.random_number(digits=2)}
    response = find_pet.by_pet_id_and_user_id(
        attributes["pet_id"], attributes["user_id"]
    )

    assert not pet_repo.select_pet_params

    assert response["success"] is False
    assert not response["data"]


def test_by_pet_id_and_user_id_failing_by_user_id():
    """testing by_pet_id_and_user_id method failing by user_id"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.random_number(digits=2), "user_id": faker.name()}
    response = find_pet.by_pet_id_and_user_id(
        attributes["pet_id"], attributes["user_id"]
    )

    assert not pet_repo.select_pet_params

    assert response["success"] is False
    assert not response["data"]
