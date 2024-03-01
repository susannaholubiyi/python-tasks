from AccountNotFoundError import *
from InvalidPinError import InvalidPinError
from account import Account


class Bank:
    def __init__(self,name):
        self.list_of_accounts = []
        self.name = name
        self.account_number = 1

    def register_customer(self, first_name, last_name, pin) -> Account:
        name = first_name + " " + last_name
        account = Account(self.account_number, name, pin)
        self.list_of_accounts.append(account)
        self.account_number += 1
        return account

    def get_number_of_customers(self):
        return len(self.list_of_accounts)

    def find_account(self, account_number) -> Account:
        for account in self.list_of_accounts:
            if account.get_account_number() == account_number:
                return account
        raise AccountNotFoundError("Account not found")

    def remove_account(self, account_number, pin):
        found_account = self.find_account(account_number)
        if found_account.validate_pin(pin):
            raise InvalidPinError("Pin is invalid")
        self.list_of_accounts.remove(found_account)

    def check_balance(self, account_number, pin):
        found_account = self.find_account(account_number)
        return found_account.check_balance(pin)

    def deposit(self, amount, account_number):
        found_account = self.find_account(account_number)
        found_account.deposit(amount)

    def withdraw(self, account_number, amount, pin):
        found_account = self.find_account(account_number)
        found_account.withdraw(amount, pin)

    def transfer(self, sender_account_number, receiver_account_number, amount, pin):
        sender_account = self.find_account(sender_account_number)
        receiver_account = self.find_account(receiver_account_number)
        sender_account.withdraw(amount, pin)
        receiver_account.deposit(amount)


# def __repr__(self):
      #  return self.
