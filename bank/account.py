from InsufficientFundError import InsufficientFundError
from InvalidAmountError import InvalidAmountError
from InvalidPinError import InvalidPinError
from diarymodule.exception.invalididerror import InvalidInputError


class Account:
    @staticmethod
    def validate_pin_length(pin):
        if not pin.isdigit():
            raise InvalidInputError("Pin must be composed only of digits")

        if len(pin) != 4:
            raise InvalidPinError("Pin must be four characters")

    def __init__(self, account_number, name: str, pin):
        self.validate_pin_length(pin)
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        if amount is None:
            raise InvalidInputError("Invalid input")

        if amount < 0:
            raise InvalidAmountError("Invalid Amount")
        self.balance += amount

    def check_balance(self, pin):
        self.check_if_input_is_empty(pin)
        self.validate_pin(pin)
        return self.balance

    def withdraw(self, amount, pin):
        self.validate_pin(pin)
        if amount < 0:
            raise InvalidAmountError("Enter a valid amount!")
        if amount > self.balance:
            raise InsufficientFundError("Balance is insufficient, would you like to deposit?")
        self.balance -= amount

    def validate_pin(self, pin: str):
        if self.pin != pin:
            raise InvalidPinError("Invalid pin")

    def get_account_number(self) -> int:
        return self.account_number

    @staticmethod
    def check_if_input_is_empty(user_input):
        if len(user_input) == 0:
            raise InvalidInputError("Invalid input")
