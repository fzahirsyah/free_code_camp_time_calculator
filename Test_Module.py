import unittest
from Time_Calculator import time_calculator


class unittest(unittest.TestCase):
    def test_add_time(self):
        actual = time_calculator("3:00 PM", "3:10")
        expected = " Expected Returns: 6:10 PM"
        self.assertEqual(actual, expected, "The test run succesfuly")

    def test_add_day(self):
        actual = time_calculator("11:30 AM", "2:32", "Monday")
        expected ="Expected Returns: 2:02 PM, Monday"
        self.assertEqual(actual, expected, "The test run succesfuly")

    def test_add_minutes(self):
        actual = time_calculator("11:43 AM", "00:20")
        expected = "Expected Returns: 12:03 PM"
        self.assertEqual(actual, expected, "The test run succesfuly")

    def test_add_next_day(self):
        actual = time_calculator("10:10 PM", "3:30")
        expected = "Expected Returns: 1:40 AM (next day)"
        self.assertEqual(actual, expected, "The test run succesfuly")

    def test_add_days(self):
        actual = time_calculator("11:43 PM", "24:20", "tueSday")
        expected = "Expected Returns: 12:03 AM, Thursday (2 days later)"
        self.assertEqual(actual, expected, "The test run succesfuly")

    def test_add_more_days(self):
        actual = time_calculator("6:30 PM", "205:12")
        expected = "Expected Returns: 7:42 AM (9 days later)"
        self.assertEqual(actual, expected, "The test run succesfuly")
    

if __name__ == "__main__":
    unittest.main()
