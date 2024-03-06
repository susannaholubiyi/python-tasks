from diarymodule.diaries import Diaries
from diarymodule.exception.DiaryIsLockedError import KeyboardInterruptError, DiaryIsLockedError
from diarymodule.exception.IncorrectPasswordError import IncorrectPasswordError
from diarymodule.exception.diarydoesnotexisterror import DiaryDoesNotExistError
from diarymodule.exception.invalididerror import InvalidIdError


class MainDiary:
    def __init__(self):
        self.diaries = Diaries()

    # def found_diary(self, user_name):
    #     diary = self.diaries.find_diary(user_name)
    #     return diary

    def main_menu(self):
        menu = """
                **************** Welcome to your Diary ******************
                                         
                Enter any of the following numbers to carry out an action
                1-> Create diary
                2-> Unlock diary
                3-> Create entry
                4-> Find entry by Id
                5-> Update entry
                6-> Delete entry
                7-> Delete diary
                8-> Exit App
                 
                **********************************************************
                Select option:
                """
        choice = input(menu)
        match choice:
            case "1":
                user_name = input("Enter your user name: ")
                password = input("Enter your password: ")
                try:
                    self.diaries.add(user_name, password)
                    print("Your diary has been created, unlock with password to add entry")
                    print("Always remember your password")
                except (IncorrectPasswordError, KeyboardInterruptError) as e:
                    print(e)
                finally:
                    self.main_menu()
            case "2":
                user_name = input("Enter your user name to find diary: ")
                try:
                    diary = self.diaries.find_diary(user_name)
                    password = input("Enter your password: ")
                    diary.unlock_diary(password)
                    print("your diary has been unlocked ")
                except (DiaryDoesNotExistError, IncorrectPasswordError, KeyboardInterruptError) as e:
                    print(e)
                finally:
                    self.main_menu()

            case "3":
                user_name = input("Enter your user name to find diary: ")
                try:
                    diary = self.diaries.find_diary(user_name)
                    title = input("Enter the title of your new entry: ")
                    body = input("Enter the body of your new entry:")
                    diary.create_entry(title, body)
                    print("Your ID is", diary.get_number_of_entries())
                    print("Your entry has been added")
                except (DiaryDoesNotExistError, KeyboardInterruptError, DiaryIsLockedError) as e:
                    print(e)
                finally:
                    self.main_menu()
            case "4":
                user_name = input("Enter your user name to find diary: ")
                try:
                    diary = self.diaries.find_diary(user_name)
                    i_d = input("Enter your ID: ")
                    entry = diary.find_entry(int(i_d))
                    print(entry)
                except (DiaryDoesNotExistError,DiaryIsLockedError, InvalidIdError, KeyboardInterruptError) as e:
                    print(e)
                finally:
                    self.main_menu()
            case "5":
                user_name = input("Enter your user name to find diary: ")
                try:
                    diary = self.diaries.find_diary(user_name)
                    i_d = input("Enter your ID: ")
                    new_title = input("Enter the new title: ")
                    new_body = input("Enter the new body")
                    diary.update_entry(int(i_d), new_title, new_body)
                    print("Entry has been updated")
                except (DiaryDoesNotExistError, DiaryIsLockedError, InvalidIdError, KeyboardInterruptError) as e:
                    print(e)
                finally:
                    self.main_menu()
            case "6":
                user_name = input("Enter your user name to find diary: ")
                try:
                    diary = self.diaries.find_diary(user_name)
                    i_d = input("Enter your ID: ")
                    diary.delete_entry(int(i_d))
                    print("Entry has been deleted")
                except (DiaryDoesNotExistError, DiaryIsLockedError, InvalidIdError, KeyboardInterruptError) as e:
                    print(e)
                finally:
                    self.main_menu()
            case "7":
                user_name = input("Enter your user name to find diary: ")
                try:
                    self.diaries.find_diary(user_name)
                    password = input("Enter your password: ")
                    self.diaries.delete_diary(user_name, password)
                    print("Diary has been deleted")
                except (DiaryDoesNotExistError, DiaryIsLockedError, KeyboardInterruptError) as e:
                    print(e)
                finally:
                    self.main_menu()

            case "8":
                exit(69)
            case _:
                self.main_menu()


if __name__ == "__main__":
    main_diary = MainDiary()
    main_diary.main_menu()
