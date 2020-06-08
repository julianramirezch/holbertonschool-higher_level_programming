#!/usr/bin/python3
""" Base rectangle tester """
import unittest
import pep8
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests base documentation """

    def test_pep8(self):
        """ Test that models/base.py conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 Style")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(Base.__doc__)

    def test_docmodule(self):
        """ Tests module """
        self.assertTrue(len(Base.__doc__) >= 1)


class TestRectangleFunctions(unittest.TestCase):
    ''' tester for rectagle functions '''

    def test_init(self):
        r1 = Rectangle(2, 3, 1, 1, 10)
        self.assertIsInstance(r1, Rectangle)

    def test_id(self):
        r2 = Rectangle(2, 5, 1, 1, 10)
        self.assertIsNotNone(id(r2))
        self.assertEqual(r2.id, 10)

    def test_args(self):
        r3 = Rectangle(10, 20, 10, 10)
        self.assertEqual(r3.x, 10)
        self.assertEqual(r3.height, 20)
        self.assertEqual(r3.y, 10)
        self.assertEqual(r3.width, 10)

    def test_kwargs(self):
        r4 = Rectangle(width=5, height=10, x=15, y=20, id=100)
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 10)
        self.assertEqual(r4.x, 15)
        self.assertEqual(r4.y, 20)
        self.assertEqual(r4.id, 100)

    def test_update_kwargs(self):
        r4 = Rectangle(2, 5, 1, 1, 10)
        r4.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.y, 3)
        self.assertEqual(r4.width, 4)

    def test_update_args_present(self):
        r4 = Rectangle(2, 5, 1, 1, 10)
        r4.update(20, height=2, y=3, width=4)
        self.assertEqual(r4.id, 20)
        self.assertEqual(r4.width, 4)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.y, 3)

    def test_update_no_args(self):
        """ Send no arguments to update """
        Base._Base__nb_objects = 0
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_width_values(self):
        self.assertRaises(TypeError, Rectangle, 'a', 'b')

    def test_width_message_errors(self):
        """ Send non int arguments for width """
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("holberton", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((1, 2), 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([3, 4], 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({'key': 1}, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(5.25, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_message_errors(self):
        """ Send non int arguments for width """
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "holberton")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, (1, 2))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, [3, 4])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, {'key': 1})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, 5.25)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_message_errors(self):
        """ Send arguments for x """
        r = Rectangle(10, 10, 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 10, "holberton")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 10, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 10, (1, 2))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 10, [3, 4])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 10, {'key': 1})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 10, 5.25)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(10, 10, -10)

    def test_y_message_errors(self):
        """ Send non int arguments for width """
        r = Rectangle(10, 10, 8, 8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 10, 8, "holberton")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 10, 8, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 10, 8, (1, 2))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 10, 8, [3, 4])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 10, 8, {'key': 1})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 10, 8, 5.25)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(10, 10, 8, -10)

    def test_area_results(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """ Test display function """
        sys.stdout = io.StringIO()
        r4 = Rectangle(3, 3)
        r4.display()
        self.assertEqual(sys.stdout.getvalue(), "###\n###\n###\n")

    def test_display_xy(self):
        """checks display xy"""
        Base._Base__nb_objects = 0
        r5 = Rectangle(2, 3, 2, 2)
        old_stdout = sys.stdout
        result = io.StringIO()
        sys.stdout = result
        r5.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        Base._Base__nb_objects = 0
        r6 = Rectangle(3, 3, 0, 0, 1)
        string_rep = r6.__str__()
        self.assertEqual(string_rep, "[Rectangle] (1) 0/0 - 3/3")

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0
        r7 = Rectangle(10, 2, 1, 9, 1)
        r7_dictionary = r7.to_dictionary()
        self.assertEqual({"id": 1, "width": 10, "height": 2, "x": 1, "y": 9},
                         r7_dictionary)
