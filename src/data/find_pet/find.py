from typing import Type, Dict, List
from src.domain.use_cases.find_pet import FindPet as FindPetInterface
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.models import Pets


class FindPet(FindPetInterface):
    """Class to define use case Find Pet"""

    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet by id
        :param - pet_id: id of the Pet
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"success": validate_entry, "data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Select Pet by owner id
        :param - user_id: id of a owner
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"success": validate_entry, "data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Select Pet by pet id and user_id
        :param - pet_id: id of the Pet
               - user_id: id of the owner
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

        return {"success": validate_entry, "data": response}
