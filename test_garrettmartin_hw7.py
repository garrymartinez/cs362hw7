import unittest
import garrettmartin_hw7

class TestClass(unittest.TestCase):
#-----------------------------------------------------------------------------
# Tests for fizzbuzz method
#-----------------------------------------------------------------------------
    def test_fizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(2), "Fizz")

if __name__ == "__main__":
    unittest.main()
