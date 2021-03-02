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

    def test_fizzbuzz(self):
        self.assertEqual(garrettmartin_hw7.fizzbuzz(14), "FizzBuzz")

#-----------------------------------------------------------------------------
# Tests for leapyear method
#-----------------------------------------------------------------------------
    def test_leapyear(self):
        self.assertEqual(garrettmartin_hw7.leapyear(2004), True)

    def test_divisible100(self):
        self.assertEqual(garrettmartin_hw7.leapyear(1500), False)

if __name__ == "__main__":
    unittest.main()
