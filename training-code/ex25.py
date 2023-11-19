import unittest
from my_utils import factorial


class FactorialTests(unittest.TestCase):

    def test_factorial_of_positive_int(self):
        actual = factorial(5)
        expected = 120
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
