"""Test the prime checker functions"""
import unittest
from prime_checker import is_prime, find_primes_up_to, list_primes_in_range

class TestPrimeChecker(unittest.TestCase):
    """Test the prime checker functions"""
    def test_is_prime(self)->None:
        """Test the is_prime function with various inputs"""
        # Test prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(23))
        # Test non-prime numbers
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(25))
    def test_find_primes_up_to(self)->None:
        """Test finding primes up to a limit"""
        self.assertEqual(find_primes_up_to(10), [2, 3, 5, 7])
        self.assertEqual(find_primes_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(find_primes_up_to(1), [])
        self.assertEqual(find_primes_up_to(2), [2])
    def test_list_primes_in_range(self)->None:
        """Test listing primes within a specific range"""
        self.assertEqual(list_primes_in_range(10, 20), [11, 13, 17, 19])
        self.assertEqual(list_primes_in_range(1, 10), [2, 3, 5, 7])
        self.assertEqual(list_primes_in_range(20, 30), [23, 29])
        self.assertEqual(list_primes_in_range(1, 1), [])
    def test_main_function_exceptions(self)->None:
        """Test exception handling in main function"""
        # This would require mocking input() and testing the exception paths
        # We'll need to modify the main function slightly to make it more testable
        pass
if __name__ == '__main__':
    """Run the tests"""
    unittest.main()
