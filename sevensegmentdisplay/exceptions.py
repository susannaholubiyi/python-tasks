class InvalidInputError(BaseException):
    def __int__(self,message):
        super().__init__(message)