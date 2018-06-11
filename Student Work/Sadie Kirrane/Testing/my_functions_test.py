import unittest
from my_functions import *

class TestMaxNumber(unittest.TestCase):

	def test_highest_of_3(self):
		self.assertEqual(max_of_3(2, 8, 1), 8)
		
		def test_all_equal(self):
			self.assertEqual(max_of_3(5, 5, 5), 5)

# class TestIsEven(unittest.TestCase):

# 	def test_even(self):
# 		self.assertTrue(is_even(10))


# 	def test_odd(self):
# 		self.assertFalse(is_even(5))


# class TestSQRT(unittest.TestCase):
# 	def Test 
# 		self.assertEqual(4, 2)


# if __name__ == '__main__':
# 	unittest.main()