from faker import Faker
from src.domain.models import Users

faker = Faker()


def mock_user() -> Users:
    """Mocking Users"""

    return Users(
        id=faker.random_number(digits=4), name=faker.name(), password=faker.name()
    )
