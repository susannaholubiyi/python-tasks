import unittest

from InsufficientFundError import InsufficientFundError
from InvalidAmountError import InvalidAmountError
from InvalidPinError import InvalidPinError
from account import Account


class MyTestCase(unittest.TestCase):
    def test_account_can_deposit(self):
        account: Account = Account(1, "name", "0000", )
        account.deposit(1000)
        self.assertEquals(1000, account.check_balance("0000"))

    def test_deposit_2k_withdraw1k_customer(self):
        account: Account = Account(1, "name", "0000")
        account.deposit(2000)
        account.withdraw(1000, "0000")
        self.assertEquals(1000, account.check_balance("0000"))

    def test_deposit10k_withdraw1500_balance_is8500(self):
        account: Account = Account(1, "name", "1111")
        account.deposit(10_000)
        account.withdraw(1500, "1111")
        self.assertEquals(8500, account.check_balance("1111"))

    def test_that_depositing_less_than_zero_throws_invalid_amount_exception(self):
        account: Account = Account(1, "name", "0000")
        with self.assertRaises(InvalidAmountError):
            account.deposit(-1000)

    def test_deposit5k_withdraw6k_insufficient_funds_exception_is_thrown(self):
        account: Account = Account(1, "name", "0000")
        with self.assertRaises(InsufficientFundError):
            account.withdraw(10000, "0000")

    def test_deposit5k_withdraw_minus5k_insufficient_funds_exception_is_thrown(self):
        account: Account = Account(1, "name", "0000")
        with self.assertRaises(InsufficientFundError):
            account.withdraw(-5_000, "0000")

    def test_that_withdraw_with_wrong_pin_raises_invalid_pin_error(self):
        account: Account = Account(1, "name", "0000")
        account.deposit(10_000)
        with self.assertRaises(InvalidPinError):
            account.withdraw(5000, 1111)

    def test_that_check_balance_with_wrong_pin_raises_invalid_pin_error(self):
        account: Account = Account(1, "name", "0000")
        account.deposit(10_000)
        with self.assertRaises(InvalidPinError):
            account.check_balance(1111)


