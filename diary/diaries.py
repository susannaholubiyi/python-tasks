from diarymodule.diary import Diary
from diarymodule.exception.IncorrectPasswordError import IncorrectPasswordError
from diarymodule.exception.diarydoesnotexisterror import DiaryDoesNotExistError
from diarymodule.exception.invalididerror import InvalidInputError


def check_if_string_is_empty(user_name):
    if len(user_name) == 0:
        raise InvalidInputError("Invalid input")


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, user_name: str, password: str):
        check_if_string_is_empty(user_name)
        check_if_string_is_empty(password)
        diary = Diary(user_name, password)
        self.diaries.append(diary)

    def find_diary(self, user_name: str):
        check_if_string_is_empty(user_name.strip())
        for diary in self.diaries:
            if diary.user_name == user_name:
                return diary
        raise DiaryDoesNotExistError("Diary does not exist")

    def delete_diary(self, user_name, password):
        check_if_string_is_empty(user_name)
        check_if_string_is_empty(password)
        found_diary = self.find_diary(user_name)
        self.validate_password(password)
        self.diaries.remove(found_diary)

    def validate_password(self, password):
        for diary in self.diaries:
            if diary.password == password:
                return True
        raise IncorrectPasswordError("Password is incorrect")

    def get_number_of_diaries(self):
        return len(self.diaries)
