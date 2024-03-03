import unittest
from AccountNotFoundError import AccountNotFoundError
from InsufficientFundError import InsufficientFundError
from InvalidAmountError import InvalidAmountError
from InvalidPinError import InvalidPinError

from bank import Bank


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("SBbank")

    def test_that_bank_can_register_one_customer(self):
        self.bank.register_customer("first name", "last name", "0000")
        self.assertEquals(1, self.bank.get_number_of_customers())

    def test_that_customer_register_with_invalid_pin_invalid_pin_error_is_raised(self):
        self.assertRaises(InvalidPinError, lambda: self.bank.register_customer("seyi", "seun","111"))

    def test_that_bank_can_register_customer_and_find_account(self):
        account1 = self.bank.register_customer("first name", "last name", "0000")
        self.assertEquals(account1, self.bank.find_account(1))

    def test_that_bank_did_not_registers_customer_and_number_of_customer_is_zero(self):
        self.assertEquals(0, self.bank.get_number_of_customers())

    def test_that_bank_cannot_find_account_that_does_not_exist(self):
        self.assertRaises(AccountNotFoundError, lambda: self.bank.find_account(1111))

    def test_that_bank_registers_two_customers_delete_second_first_customer_remains(self):
        account1 = self.bank.register_customer("Suzie", "Barbie", "0000")
        self.bank.register_customer("joy", "olajide", "1111")
        self.bank.remove_account(2, "1111")
        self.assertEquals(account1, self.bank.find_account(1))

    def test_that_bank_registers_two_customers_delete_first_customer_only_second_customer_remains(self):
        self.bank.register_customer("Suzie", "Barbie", "0000")
        account2 = self.bank.register_customer("joy", "olajide", "1111")
        self.bank.remove_account(1, "0000")
        self.assertEquals(account2, self.bank.find_account(2))
        self.assertEquals(1, self.bank.get_number_of_customers())

    def test_that_bank_can_register_three_customer_delete_second_customer_and_find_first_and_last_customer(self):
        account1 = self.bank.register_customer("Sharon", "olubiyi", "1234")
        self.bank.register_customer("Suzie", "Barbie", "0000")
        account3 = self.bank.register_customer("joy", "olajide", "1111")
        self.bank.remove_account(2, "0000")
        self.assertEquals(account1, self.bank.find_account(1))
        self.assertEquals(account3, self.bank.find_account(3))
        self.assertEquals(2, self.bank.get_number_of_customers())

    def test_deposit2k_into_account_balance_is2k_test(self):
        self.bank.register_customer("Suki", "love", "0000")
        self.assertEquals(0, self.bank.check_balance(1, "0000"))
        self.bank.deposit(2_000, 1)
        self.assertEquals(2_000, self.bank.check_balance(1, "0000"))

    def test_register_three_customers_remove_second_customer_add_fourth_customer_remove_third_customer(self):
        self.bank.register_customer("Joy", "Olajide", "0000")
        self.bank.register_customer("Seyi", "Olubiyi", "1111")
        self.bank.register_customer("Susannah", "Olubiyi", "1234")
        self.bank.remove_account(2, "1111")
        self.bank.register_customer("Shalom", "Olubiyi", "1010")
        self.assertEquals(3, self.bank.get_number_of_customers())
        self.bank.remove_account(3, "1234")
        self.assertEquals(2, self.bank.get_number_of_customers())
        self.assertIsNotNone(self.bank.find_account(1))
        self.assertIsNotNone(self.bank.find_account(4))

    def test_that_if_customer_deposits_negative_amount_invalid_amount_error_is_raised(self):
        account1 = self.bank.register_customer("Joy", "Olajide", "0000")
        self.assertEquals(account1, self.bank.find_account(1))
        with self.assertRaises(
                InvalidAmountError):
            self.bank.deposit(-1000, 1)

    def test_register_two_customers_deposit2k_into_second_customer_account_second_customer_balance_is2k(self):
        self.bank.register_customer("Joy", "Olajide", "0000")
        self.bank.register_customer("Seyi", "Olubiyi", "1111")
        self.bank.deposit(2_000, 2)
        self.assertEquals(0, self.bank.check_balance(1, "0000"))
        self.assertEquals(2_000, self.bank.check_balance(2, "1111"))

    def test_register_two_customers_deposit2k_into_first_customer_account_first_customer_balance_is2k(self):
        self.bank.register_customer("Seun", "Olubiyi", "0000")
        self.bank.register_customer("Seyi", "Olubiyi", "1111")
        self.bank.deposit(2_000, 1)
        self.assertEquals(2_000, self.bank.check_balance(1, "0000"))
        self.assertEquals(0, self.bank.check_balance(2, "1111"))

    def test_register_two_customers_deposit2k_into_second_customer_account_withdraw1k_balance_is1k(self):
        self.bank.register_customer("Seun", "Olubiyi", "0000")
        self.bank.register_customer("Seyi", "Olubiyi", "1111")
        self.bank.deposit(2_000, 2)
        self.bank.withdraw(2, 1_000, "1111")
        self.assertEquals(1_000, self.bank.check_balance(2, "1111"))

    def test_that_withdrawing_without_depositing_will_raise_an_insufficient_funds_error(self):
        self.bank.register_customer("Susannah", "Olubiyi", "0000")
        self.assertRaises(InsufficientFundError, lambda: self.bank.withdraw(1, 1000, "0000"))

    def test_that_customer_one_can_transfer2k_to_second_customer(self):
        self.bank.register_customer("Susannah", "Olubiyi", "0000")
        self.bank.register_customer("Joy", "Olajide", "1111")
        self.bank.deposit(10_000, 1)
        self.bank.transfer(1, 2, 3_000, "0000")
        self.assertEquals(7_000, self.bank.check_balance(1, "0000"))
        self.assertEquals(3_000, self.bank.check_balance(2, "1111"))

    def test_that_that_when_i_deposit5k_into_account1_and_transfer6k_into_account2_insufficient_balance_error_is_raised(self):
        self.bank.register_customer("Susannah", "Olubiyi", "0000")
        self.bank.register_customer("Joy", "Olajide", "1111")
        self.bank.deposit(5_000, 1)
        self.assertRaises(InsufficientFundError, lambda: self.bank.transfer(1, 2, 6000, "0000"))

    def test_that_bank_registers_two_accounts_delete_the_first_and_try_to_transfer_to_deleted_account(self):
        self.bank.register_customer("Susannah", "Olubiyi", "0000")
        self.bank.register_customer("Joy", "Olajide", "1111")
        self.bank.remove_account(1, "0000")
        self.bank.deposit(500_000, 2)
        self.assertRaises(AccountNotFoundError, lambda: self.bank.transfer(2, 1, 100_000, "0000"))

    def test_that_bank_registers_two_accounts_delete_the_second_and_try_to_transfer_to_deleted_account(self):
        self.bank.register_customer("Susannah", "Olubiyi", "0000")
        self.bank.register_customer("Joy", "Olajide", "1111")
        self.bank.remove_account(2, "1111")
        self.bank.deposit(500_000, 1)
        self.assertRaises(AccountNotFoundError, lambda: self.bank.transfer(1, 2, 100_000, "0000"))
