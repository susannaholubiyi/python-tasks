import unittest

from diarymodule.diaries import Diaries


class DiariesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.diaries = Diaries()

    def test_that_diaries_can_add_diary(self):
        self.diaries.add("seyi", "1111")
        self.assertEqual(1, self.diaries.get_number_of_diaries())

    def test_that_diaries_can_add_three_diaries(self):
        self.diaries.add("seyi", "1111")
        self.diaries.add("seun", "0000")
        self.diaries.add("shalom", "1234")
        self.assertEqual(3, self.diaries.get_number_of_diaries())

    def test_that_diaries_adds_one_diary_and_deletes_it(self):
        self.diaries.add("seyi", "1111")
        self.diaries.delete_diary("seyi", "1111")
        self.assertEqual(0, self.diaries.get_number_of_diaries())

    def test_that_diaries_can_add_four_diaries_and_delete_two(self):
        self.diaries.add("seyi", "1111")
        self.diaries.add("seun", "0000")
        self.diaries.add("shalom", "1234")
        self.diaries.add("sharon", "1010")
        self.diaries.delete_diary("seyi", "1111")
        self.diaries.delete_diary("shalom", "1234")
        self.assertEqual(2, self.diaries.get_number_of_diaries())

    # def test_that_diaries_can_add_two_diaries_delete_the_first_and_find_the_second(self):
    #     self.diaries.add("seyi", "1111")
    #     self.diaries.add("seun", "0000")
    #     self.diaries.delete_diary("seyi", "1111")
    #     self.assertEquals("seyi", self.)