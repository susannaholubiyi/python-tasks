import unittest

from diarymodule.diary import Diary
from diarymodule.exception.DiaryIsLockedError import DiaryIsLockedError
from diarymodule.exception.IncorrectPasswordError import IncorrectPasswordError
from diarymodule.exception.invalididerror import InvalidIdError


class DiaryTestCase(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("susu", "1234")

    def test_that_diary_is_locked(self):
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_is_no_longer_locked_after_unlocking_it(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.assertFalse(self.diary.is_locked())

    def test_that_unlocking_diary_with_incorrect_password_will_raise_incorrect_password_error(self):
        self.assertTrue(self.diary.is_locked())
        self.assertRaises(IncorrectPasswordError, lambda: self.diary.unlock_diary("1111"))

    def test_that_when_you_unlock_and_lock_diary_it_is_locked(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_that_when_you_create_entry_entry_is_created(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.diary.create_entry("title", "body")
        self.assertEquals(1, self.diary.get_number_of_entries())

    def test_that_when_you_create_entry_and_delete_entry_it_is_deleted(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.diary.create_entry("title", "body")
        self.assertEquals(1, self.diary.get_number_of_entries())
        self.diary.delete_entry(1)
        self.assertEquals(0, self.diary.get_number_of_entries())

    def test_that_deleting_a_non_existent_entry_raises_an_invalid_id_error(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.assertRaises(InvalidIdError, lambda: self.diary.delete_entry(1))

    def test_that_when_you_add_four_entries_and_delete_two_two_entries_remain(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.diary.create_entry("title1", "body1")
        self.diary.create_entry("title2", "body2")
        self.diary.create_entry("title3", "body3")
        self.diary.create_entry("title4", "body4")
        self.assertEquals(4, self.diary.get_number_of_entries())
        self.diary.delete_entry(1)
        self.diary.delete_entry(2)
        self.assertEquals(2, self.diary.get_number_of_entries())

    def test_that_when_you_create_entry_and_update_entry_will_be_updated(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.diary.create_entry("title", "body")
        self.assertEquals("title", self.diary.find_entry(1).title)
        self.assertEquals("body", self.diary.find_entry(1).body)
        self.diary.update_entry(1, "new_title", "new_body")
        self.assertEquals("new_title", self.diary.find_entry(1).title)
        self.assertEquals("new_body", self.diary.find_entry(1).body)

    def test_that_when_you_create_an_entry_and_update_with_wrong_id_invalid_id_error_is_raised(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.diary.create_entry("title", "body")
        self.assertRaises(InvalidIdError, lambda: self.diary.update_entry(2, "new title", "new body"))

    def test_that_when_you_create_entry_without_unlocking_diary_error_is_raised(self):
        self.assertTrue(self.diary.is_locked())
        self.assertRaises(DiaryIsLockedError, lambda: self.diary.update_entry(2, "new title", "new body"))

    def test_that_when_you_find_entry_without_unlocking_diary_error_is_raised(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.diary.create_entry("title", "body")
        self.diary.lock_diary()
        self.assertRaises(DiaryIsLockedError, lambda: self.diary.find_entry(1))

    def test_that_when_you_update_entry_without_unlocking_diary_error_is_raised(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.diary.create_entry("title", "body")
        self.diary.lock_diary()
        self.assertRaises(DiaryIsLockedError, lambda: self.diary.update_entry(1, "new title", "new body"))

    def test_that_when_you_delete_entry_without_unlocking_diary_error_is_raised(self):
        self.assertTrue(self.diary.is_locked())
        self.diary.unlock_diary("1234")
        self.diary.create_entry("title", "body")
        self.diary.lock_diary()
        self.assertRaises(DiaryIsLockedError, lambda: self.diary.delete_entry(1))
