from faker import Faker
from src.domain.models import Pets


faker = Faker()


def mock_pet() -> Pets:
    """Mocking Pets"""
    return Pets(
        id=faker.random_number(digits=4),
        name=faker.name(),
        age=faker.random_number(digits=1),
        specie="FISH",
        user_id=faker.random_number(digits=4),
    )
