from AccountNotFoundError import AccountNotFoundError
from InsufficientFundError import InsufficientFundError
from InvalidAmountError import InvalidAmountError
from InvalidPinError import InvalidPinError
from bank import Bank
from diarymodule.exception.invalididerror import InvalidInputError


class BankApp:
    def __init__(self):
        self.bank = Bank(" Suzie Bank")

    def main_menu(self):
        menu = """
                **************** Welcome to SBBank ****************
                
                Enter any of the following numbers to carry out an action
                
                
                1-> Open an account
                2-> Deposit
                3-> Withdraw
                4-> Transfer
                5-> Check account balance
                6-> Close account
                7-> Exit App
                
                <><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                Select option: """
        choice = input(menu)

        match choice:
            case "1":
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                pin = input("Chose your desired four digit pin:")
                try:
                    account = self.bank.register_customer(first_name, last_name, pin)
                    print("Account has been successfully opened! Here's a Barbieque for you ")
                    print("Your account number is ", account.get_account_number())
                except (InvalidPinError, InvalidInputError) as e:
                    print(e)
                finally:
                    self.main_menu()

            case "2":
                amount = input("Enter the amount you want to deposit: ")
                account_number = input("Enter your accountNumber: ")

                try:
                    self.bank.deposit(int(amount), int(account_number))
                    print(amount, " deposited successfully ")

                except (InvalidAmountError, InvalidInputError, InvalidPinError, AccountNotFoundError) as e:
                    print(e)
                finally:
                    self.main_menu()

            case "3":
                account_number = input("Enter your accountNumber: ")
                amount = input("Enter the amount you want to withdraw: ")
                pin = input("Enter your pin: ")

                try:
                    self.bank.withdraw(int(account_number), int(amount), pin)
                    print(amount, " withdrawn successfully ")

                except (AccountNotFoundError, InvalidInputError, InvalidPinError, InsufficientFundError, InvalidAmountError) as e:
                    print(e)
                finally:
                    self.main_menu()

            case "4":
                sender_account = input("Enter your accountNumber: ")
                receiver_account = input("Enter the accountNumber you want to send to: ")
                amount = input("Enter the amount you want to deposit: ")
                pin = input("Enter your pin: ")

                try:
                    self.bank.transfer(int(sender_account), int(receiver_account), int(amount), pin)
                    print("Transfer successfully done")

                except (AccountNotFoundError, InvalidInputError, InvalidPinError, InvalidAmountError, InsufficientFundError) as e:
                    print(e)
                finally:
                    self.main_menu()

            case "5":
                account_number = input("Enter your accountNumber: ")
                pin = input("Enter your pin: ")
                try:
                    balance = self.bank.check_balance(int(account_number), pin)
                    print("Your balance is: ", balance)

                except(AccountNotFoundError, InvalidInputError, InvalidPinError) as e:
                    print(e)

                finally:
                    self.main_menu()

            case "6":
                account_number = input("Enter your accountNumber: ")
                pin = input("Enter your pin: ")

                try:
                    self.bank.remove_account(int(account_number), pin)
                    print("We're sad to let you go")

                except(AccountNotFoundError, InvalidInputError, InvalidPinError) as e:
                    print(e)

                finally:
                    self.main_menu()

            case "7":
                print("Thank you for banking with us!")
                exit(69)
            case _:
                self.main_menu()


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main_menu()
