import unittest

from backtosenderlogisticmodule.backtosenderlogistics import payment_calculator


class MyTest(unittest.TestCase):
    def test_that_rider_delivers_25parcels_function_returns_9000(self):
        self.assertEquals(9000, payment_calculator(25))

    def test_that_rider_delivers_80parcels_function_returns_45000(self):
        self.assertEquals(45000, payment_calculator(80))

    def test_that_rider_delivers_50parcels_function_returns_15000(self):
        self.assertEquals(15000, payment_calculator(50))

    def test_that_rider_delivers_62parcels_function_return_20500(self):
        self.assertEquals(20500, payment_calculator(62))

    def test_that_riders_delivers_zero_function_returns_5000(self):
        self.assertEquals(5000, payment_calculator(0))
