import unittest

from training.day1.Question1Example import calculateCircleArea


class TestCalculateCircleArea(unittest.TestCase):

    def test_CalculateCircleArea(self):
        self.assertEqual(calculateCircleArea(10),10)