#!/usr/bin/python3
""" module for Rectangle unit tests """
import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):

    def setUp(self):
        """ imports module, instantiates class """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ cleans up after each test_method """
        pass

    def test_style_rect(self):
        """ tests for pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects == 0
        cls.r1 = Rectangle(10, 2)
        cls.r3 = Rectangle(2, 4, 2, 2, 12)

    def test_id(self):
        Base._Base__nb_objects = 98
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)

    def test_attr_errors(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r11 = Rectangle(10, "2")
        with self.assertRaises(ValueError, msg="height must be  > 0"):
            r11 = Rectangle(-2, 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r11 = Rectangle({1: 2}, 2)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r21 = Rectangle(10, 2)
            r21.width = -10
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r31 = Rectangle(10, 2)
            r31.x = {}
        with self.assertRaises(ValueError, msg="y must be >=0"):
            r41 = Rectangle(10, 2, 3, -1)

    def test_area(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r3.area(), 8)

    def test_display(self):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.r1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "##########\n##########\n")
        sys.stdout = mystdout = StringIO()
        self.r3.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n  ##\n  ##\n")
        sys.stdout = old_stdout

    def test_str(self):
        """ tests __str__() method return """
        r = Rectangle(5, 2)
        s = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(r), s)
        r = Rectangle(1, 1, 1)
        s = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(r), s)
        r = Rectangle(3, 4, 5, 6)
        s = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(r), s)

        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        self.r1.update(89)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 10/2")
        self.r1.update(89, 2)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 2/2")
        self.r1.update(89, 2, 3)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 2/3")
        self.r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        with self.assertRaises(ValueError, msg="x must be >=0"):
            self.r1.update(y=1, width=2, x=-3, id=89)

    def test_dictionary(self):
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r = Rectangle(1, 2)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

        r = Rectangle(1, 2, 3, 4, 5)
        d = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

        r.x = 10
        r.y = 20
        r.width = 30
        r.height = 40
        d = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(r.to_dictionary(), d)

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_to_json(self):
        dict = self.r1.to_dictionary()
        self.assertIsInstance(Base.to_json_string(dict), str)


if __name__ == '__main__':
    unittest.main()
