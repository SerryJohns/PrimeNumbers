import unittest
from PrimeNumbers import prime

class TestPrimeNumbers(unittest.TestCase):

    def setUp(self):
        self.result = prime.generate_prime_numbers(100)

    def test_only_integers(self):
        for my_number in self.result:
            self.assertIsInstance(my_number, int)

    def test_first_prime_number(self):
        self.assertEqual(self.result[0], 2)

    def test_prime_even(self):
        for my_number in self.result:
            self.assertFalse(my_number > 2 and my_number % 2 == 0)

    def test_prime_odd(self):
        for my_number in self.result:
            self.assertFalse(my_number > 3 and my_number % 3 == 0)

    def test_negative_primes(self):
        for my_number in self.result:
            self.assertFalse(my_number < 1)

    def test_list_length(self):
        self.assertEqual(len(self.result), 25)

    def test_compare_output(self):
        self.assertEqual(self.result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

if __name__ == '__main__':
    unittest.main()