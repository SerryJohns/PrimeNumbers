import unittest
from andelaSLC import prime

class TestPrimeNumbers(unittest.TestCase):

    def setUp(self):
        self.result = prime.generate_prime_numbers(10)

    def test_first_prime_number(self):
        self.assertequal(self.result[0:], 2)

    def test_prime_even(self):
        for my_number in self.result:
            self.assertFalse(my_number > 2 and my_number % 2 == 0)

    def test_prime_odd(self):
        for my_number in self.result:
            self.assertFalse(my_number > 3 and my_number % 3 == 0)


if __name__ == '__main__':
    unittest.main()