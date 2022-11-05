from typing import List, Dict
from abc import ABC, abstractmethod
from src.domain.models import Pets


class FindPet(ABC):
    """Interface to FindPet use case"""

    @abstractmethod
    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""
        raise NotImplementedError()

    @abstractmethod
    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""
        raise NotImplementedError()

    @abstractmethod
    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Specific Case"""
        raise NotImplementedError()
