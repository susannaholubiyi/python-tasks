from diarymodule.diary import Diary
from diarymodule.exception.IncorrectPasswordError import IncorrectPasswordError
from diarymodule.exception.diarydoesnotexisterror import DiaryDoesNotExistError


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, user_name, password):
        diary = Diary(user_name, password)
        self.diaries.append(diary)

    def find_diary(self, user_name):
        for diary in self.diaries:
            if diary.user_name == user_name:
                return diary
        raise DiaryDoesNotExistError("Diary does not exist")

    def delete_diary(self, user_name, password):
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
