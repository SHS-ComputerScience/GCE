import unittest
from my_function import *

# class TestIsEven(unittest.TestCase):

# 	def test_even(self):
# 		self.assertTrue(is_even(10))

# 	def test_odd(self):
# 		self.assertFalse(is_even(5))

# 	def sqrt_test(self):
# 		self.assertEqual(sqrt(10))

# class TestMaxNumber(unittest.TestCase):
	
# 	def test_highest_of_3(self):
# 		self.asserEqual(max_of_3(2, 8, 1), 8)
		
# 	def test_all_equal(self):
# 		self.assertEqual(max_of_3(5, 5, 5), 5)

class TestCountString(unittest.TestCase):

	def test_count(self):
		self.assertEqual(string_counter("Pizza"), (5, 0))

	def test_case_count(self):
		self.assertEqual(string_counter("PIZzA"), (5, 0))

	def test_space(self):
		self.assertEqual(string_counter("hello world"), (10, 1))
		
	



if __name__ == '__main__':
	unittest.main()