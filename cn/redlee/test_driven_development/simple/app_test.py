import unittest
from cn.redlee.test_driven_development.simple.app import *

"""
this is first app.
"""


class MyAppTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(sayHello(), "hello world.")


if __name__ == "__main__":
    unittest.main()
