import unittest
from Recursive_main import raddition as rsum
from fractions import Fraction


class TestRecursive(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rsum(2, 4), 6)

    def test_2(self):
        self.assertEqual(rsum(2, 3), 5)

    def test_3(self):
        self.assertTrue(rsum(1, 4))

    def test_4(self):
        self.assertEqual(Fraction(1, 3) + Fraction(1, 3), Fraction(1, 2))


if __name__ == '__main__':
    unittest.main()
