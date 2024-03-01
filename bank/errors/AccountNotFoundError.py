class AccountNotFoundError(Exception):
    def __int__(self):
        super().__init__("Account not found")
