#!/usr/bin/python3

"""Unittests for the max_integer function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Define unittests for max_integer function"""

    def test_single_element(self):
        """Test a list with single element"""
        self.assertEqual(max_integer([6]), 6)

    def test_positive_numbs(self):
        """Test a list with positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbs(self):
        """Tet a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbs(self):
        """Test a list with mixed numbers"""
        self.assertEqual(max_integer([1, -2, 3, 4, -5]), 4)

    def test_unordered_list(self):
        """Test a list with unorderd elements"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_floats(self):
        """Test a list with float elements"""
        self.assertEqual(max_integer([3.53, 9.43, -10.123, 17.2, 3.0]), 17.2)

    def test_ints_and_floats(self):
        """Test a list with mixed ints and floats"""
        self.assertEqual(max_integer([4.53, 17.5, -5, 11, 5]), 17.5)

    def test_duplicate_numbs(self):
        """Test a list with duplicate numbers"""
        self.assertEqual(max_integer([3, 2, 1, 3, 3]), 3)

    def test_string(self):
        """Test a string"""
        self.assertEqual(max_integer("Potatoes"), 't')

    def test_list_of_strings(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["John", "went", "to", "daycare"]), "went")

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
