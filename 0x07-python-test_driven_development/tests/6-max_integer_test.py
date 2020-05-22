#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """Test Max integer in list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-10, -5, -1, -2]), -1)
        self.assertEqual(max_integer([-1, -3, -4, 0]), 0)
        self.assertEqual(max_integer([-1, 0, -4, 0]), 0)

    def test_max_string(self):
        self.assertEqual(max_integer(["h", "o", "L"]), "o")

    def test_types(self):
        """Test Types in list
        """
        self.assertEqual(max_integer([1.1, 2.1, -0.3, 4]), 4)
        self.assertIs(list, list)
        self.assertEqual(max_integer([-1.1, -2.1, -0.3, -4]), -0.3)
        self.assertEqual(max_integer([-1.1, 7, -0.3, -4]), 7)

    def test_empty_list(self):
        """Test Empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_one_int(self):
        """Test one number in list
        """
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-7]), -7)

    def test_same_integer(self):
        """Test same list numbers
        """
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)
        self.assertEqual(max_integer([-7, -7, -7, -7]), -7)

    def test_raises(self):
        self.assertRaises(TypeError, max_integer, [1, 'Holberton', 3])


if __name__ == '__main__':
    unittest.main()
