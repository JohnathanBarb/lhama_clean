from typing import Dict, List
from src.domain.models import Pets
from src.domain.test import mock_pet


class FindPetSpy:
    """Class to define use_cases: FindPet"""

    def __init__(self, pet_repository: any):
        self.pet_repository = pet_repository
        self.by_pet_id_and_user_id_params = {}
        self.by_pet_id_params = {}
        self.by_user_id_params = {}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Spy Method"""

        self.by_pet_id_and_user_id_params["pet_id"] = pet_id
        self.by_pet_id_and_user_id_params["user_id"] = user_id

        response = None

        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)

        if validate_entry:
            response = [mock_pet()]

        return {"success": validate_entry, "data": response}

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Spy Method"""

        self.by_pet_id_params["pet_id"] = pet_id

        response = None

        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = [mock_pet()]

        return {"success": validate_entry, "data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Spy Method"""

        self.by_user_id_params["user_id"] = user_id

        response = None

        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_pet()]

        return {"success": validate_entry, "data": response}
