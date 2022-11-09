from typing import Dict
from src.domain.models import Users
from src.domain.test import mock_user


class RegisterUserSpy:
    """Class to define use_case: Register User"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.registry_param = {}

    def registry(self, name: str, password: str) -> Dict[bool, Users]:
        """Spy Method"""

        self.registry_param["name"] = name
        self.registry_param["password"] = password

        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = mock_user()

        return {"success": validate_entry, "data": response}
