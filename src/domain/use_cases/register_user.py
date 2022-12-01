from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class RegisterUser(ABC):
    """Interface to RegisterUser use case"""

    @abstractmethod
    def registry(self, name: str, password: str) -> Dict[bool, Users]:
        """Case"""
        raise NotImplementedError()
