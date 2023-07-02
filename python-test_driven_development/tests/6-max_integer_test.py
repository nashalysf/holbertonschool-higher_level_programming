#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        self.assertEqual(max_integer([3]), 3)

    def test_positive(self):
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)

    def test_mix_int(self):
        self.assertEqual(max_integer([0, -2, 3, 1, -4]), 3)

    def test_negative(self):
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)


if __name__ == '__main__':
    unittest.main()
