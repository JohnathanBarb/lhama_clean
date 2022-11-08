class HttpErrors:
    """Class to define errors in http"""

    @staticmethod
    def error_422():
        """HTTP 422"""

        return {"status_code": 422, "error": "Unprocessable Entity"}

    @staticmethod
    def error_400():
        """HTTP 400"""

        return {"status_code": 400, "error": "Bad Request"}
