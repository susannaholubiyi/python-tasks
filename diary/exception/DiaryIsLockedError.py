class DiaryIsLockedError(BaseException):
    def __init__(self, message):
        super().__init__(message)


class KeyboardInterruptError(KeyboardInterrupt):
    def __init__(self, message):
        super().__init__(message)
