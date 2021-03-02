import unittest
import garrettmartin_hw7

class TestClass(unittest.TestCase):
#-----------------------------------------------------------------------------
# Tests for fizzbuzz method
#-----------------------------------------------------------------------------
    def test_fizz(self):
        self.assertEqual(garrettmartin_hw7.fizzbuzz(2), "Fizz")

    def test_buzz(self):
        self.assertEqual(garrettmartin_hw7.fizzbuzz(4), "Buzz")

if __name__ == "__main__":
    unittest.main()
