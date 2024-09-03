# tests/test_main.py

import unittest
from example.main import greet

class TestMain(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
