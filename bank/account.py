from InsufficientFundError import InsufficientFundError
from InvalidAmountError import InvalidAmountError
from InvalidPinError import InvalidPinError


class Account:
    def __init__(self, account_number, name: str, pin):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountError("Invalid Amount")
        self.balance += amount

    def check_balance(self, pin):
        self.validate_pin(pin)
        return self.balance

    def withdraw(self, amount, pin):
        self.validate_pin(pin)

        if amount > self.balance or amount < 0:
            raise InsufficientFundError("Balance is insufficient, would you like to deposit?")
        self.balance -= amount

    def validate_pin(self, pin):
        if self.pin != pin or len(self.pin) != 4:
            raise InvalidPinError("Incorrect pin")

    def get_account_number(self) -> int:
        return self.account_number
