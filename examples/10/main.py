# This file shows you how to test in Python
#
# The unittest module is used to test your code
#
# For example:
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
# This will output the following:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
# You can also run the tests with the following command:
# python -m unittest main.py
# This will output the following:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#