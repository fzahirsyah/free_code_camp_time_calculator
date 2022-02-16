import unittest
from Time_Calculator import time_calculator
from unittest import main


class unittest(unittest.TestCase):
    def test_add_time(self):
        actual = time_calculator("3:00 PM", "3:10")
        expected = "6:10 PM"
        self.assertEqual(actual, expected, "Error in fucntion add time")

    def test_add_day(self):
        actual = time_calculator("11:30 AM", "2:32", "Monday")
        expected ="2:02 PM, Monday"
        self.assertEqual(actual, expected, "Error: function add day")

    def test_add_minutes(self):
        actual = time_calculator("11:43 AM", "00:20")
        expected = "12:03 PM"
        self.assertEqual(actual, expected, "Error: function add minutes")

    def test_add_next_day(self):
        actual = time_calculator("10:10 PM", "3:30")
        expected = "1:40 AM (next day)"
        self.assertEqual(actual, expected, "Error: function add next day")

    def test_add_days(self):
        actual = time_calculator("11:43 PM", "24:20", "tueSday")
        expected = "12:03 AM, Thursday (2 days later)"
        self.assertEqual(actual, expected, "Error: Function add days")

    def test_add_more_days(self):
        actual = time_calculator("6:30 PM", "205:12")
        expected = "7:42 AM (9 days later)"
        self.assertEqual(actual, expected, "Error: functions add more days")
    

if __name__ == "__main__":
    unittest.main()
