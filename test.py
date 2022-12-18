import unittest
from lab5 import factorial

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(factorial(4),24)
    def test2(self):
        self.assertEqual(factorial(1),1)
    def test3(self):
        self.assertEqual(factorial(5),120)                