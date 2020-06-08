#!/usr/bin/python3
""" Square tests """
import unittest
import pep8
import sys
import io
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """ Tests base documentation """

    def test_pep8(self):
        """ Test that models/base.py conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(Square.__doc__)

    def test_docmodule(self):
        """ Tests module """
        self.assertTrue(len(Square.__doc__) >= 1)


class TestSquareFunctions(unittest.TestCase):

    def test_init(self):
        s1 = Square(2, 1, 1, 10)
        self.assertIsInstance(s1, Square)

    def test_id(self):
        s2 = Square(2, 1, 1, 10)
        self.assertIsNotNone(id(s2))
        self.assertEqual(s2.id, 10)

    def test_args(self):
        s3 = Square(10, 20, 10, 10)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 20)
        self.assertEqual(s3.y, 10)
        self.assertEqual(s3.id, 10)

    def test_kwargs(self):
        s4 = Square(size=5, x=15, y=20, id=100)
        self.assertEqual(s4.size, 5)
        self.assertEqual(s4.x, 15)
        self.assertEqual(s4.y, 20)
        self.assertEqual(s4.id, 100)

    def test_update_kwargs(self):
        s4 = Square(2, 5, 1, 10)
        s4.update(x=1, size=2, y=3)
        self.assertEqual(s4.x, 1)
        self.assertEqual(s4.size, 2)
        self.assertEqual(s4.y, 3)

    def test_update_args_present(self):
        s4 = Square(2, 5, 1, 10)
        s4.update(20, size=8, y=3)
        self.assertEqual(s4.id, 20)
        self.assertEqual(s4.size, 8)
        self.assertEqual(s4.x, 5)
        self.assertEqual(s4.y, 3)

    def test_update_no_args(self):
        """ Send no arguments to update """
        Base._Base__nb_objects = 0
        s = Square(1, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_width_values(self):
        self.assertRaises(TypeError, Square, 'a', 'b')

    def test_width_message_errors(self):
        """ Send non int arguments for width """
        s = Square(10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("holberton")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square((1, 2))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square([3, 4])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square({'key': 1})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(5.25)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_x_message_errors(self):
        """ Send arguments for x """
        s = Square(10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(10, "holberton")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(10, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(10, (1, 2))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(10, [3, 4])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(10, {'key': 1})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(10, 5.25)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(10, -10)

    def test_y_message_errors(self):
        """ Send non int arguments for width """
        s = Square(10, 10, 8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(10, 10, "holberton")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(10, 10, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(10, 10, (1, 2))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(10, 10, [3, 4])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(10, 10, {'key': 1})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(10, 10, 5.25)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(10, 10, -10)

    def test_area_results(self):
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

        s2 = Square(5)
        self.assertEqual(s2.area(), 25)

        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.area(), 64)

    def test_display(self):
        """ Test display function """
        sys.stdout = io.StringIO()
        s4 = Square(3)
        s4.display()
        self.assertEqual(sys.stdout.getvalue(), "###\n###\n###\n")

    def test_display_xy(self):
        """checks display xy"""
        Base._Base__nb_objects = 0
        s5 = Square(2, 3, 2)
        old_stdout = sys.stdout
        result = io.StringIO()
        sys.stdout = result
        s5.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, '\n\n   ##\n   ##\n')

    def test_str(self):
        Base._Base__nb_objects = 0
        s6 = Square(3, 0, 0, 1)
        string_rep = s6.__str__()
        self.assertEqual(string_rep, "[Square] (1) 0/0 - 3")

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0
        s7 = Square(10, 2, 1, 9)
        s7_dictionary = s7.to_dictionary()
        self.assertEqual({"id": 9, "size": 10, "x": 2, "y": 1},
                         s7_dictionary)
