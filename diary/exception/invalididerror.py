class InvalidIdError(BaseException):
    def __init__(self, message):
        super().__init__(message)


class InvalidInputError(BaseException):
    def __init__(self, message="Invalid input"):
        super().__init__(message)
