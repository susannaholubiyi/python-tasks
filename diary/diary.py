from diarymodule.entry import Entry
from diarymodule.exception.DiaryIsLockedError import DiaryIsLockedError
from diarymodule.exception.IncorrectPasswordError import IncorrectPasswordError
from diarymodule.exception.invalididerror import InvalidIdError, InvalidInputError


class Diary:

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.entries = []
        self._is_locked = True
        self.number_of_entries = 1

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, _user_name):
        self._user_name = _user_name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, _password):
        self._password = _password

    def is_locked(self):
        return self._is_locked

    def unlock_diary(self, password):
        self.check_if_input_is_empty(password)
        if self.password != password:
            raise IncorrectPasswordError("password is incorrect")
        self._is_locked = False

    def lock_diary(self):
        self._is_locked = not self._is_locked

    def create_entry(self, title, body):
        self.check_if_input_is_empty(title)
        self.check_if_input_is_empty(body)
        self.validate_is_locked()
        new_entry = Entry(self.number_of_entries, title, body)
        self.entries.append(new_entry)
        self.number_of_entries += 1

    def validate_is_locked(self):
        if self._is_locked:
            raise DiaryIsLockedError("unlock diary")

    def get_number_of_entries(self):
        return len(self.entries)

    def delete_entry(self, i_d):
        if i_d is None:
            raise InvalidInputError("Invalid input")
        self.validate_is_locked()
        self.entries.remove(self.find_entry(i_d))

    def find_entry(self, i_d):
        if i_d is None:
            raise InvalidInputError("Invalid input")
        self.validate_is_locked()
        for entry in self.entries:
            if entry.get_i_d() == i_d:
                return entry
        raise InvalidIdError("Id is invalid, Entry does not exist")

    def update_entry(self, i_d, new_title, new_body):
        if i_d is None:
            raise InvalidInputError("Invalid input")
        self.check_if_input_is_empty(new_title)
        self.check_if_input_is_empty(new_body)
        self.validate_is_locked()
        found_entry = self.find_entry(i_d)
        found_entry.body = new_body
        found_entry.title = new_title

    @staticmethod
    def check_if_input_is_empty(user_input):
        if len(user_input) == 0:
            raise InvalidInputError("Invalid input")

    def __repr__(self):
        return f"{self.user_name} {self.password}"
