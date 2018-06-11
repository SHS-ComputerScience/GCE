import unittest
from my_functions import *

# ---------------------------------------------------------------------------------------------------------------------------------------
# Is Even Test
# ---------------------------------------------------------------------------------------------------------------------------------------

# class TestIsEven(unittest.TestCase):
# 	def test_even(self):
# 		self.assertTrue(is_even(10))
# 	def test_odd(self):
# 		self.assertFalse(is_even(5))

# ---------------------------------------------------------------------------------------------------------------------------------------
# Square Root Test
# ---------------------------------------------------------------------------------------------------------------------------------------

# class TestSQRT(unittest.TestCase):
# 	def test_sqrt(self):
# 		self.assertEqual(is_sqrt(9), 3)
# 	def test_none(self):
# 		self.assertEqual(is_sqrt(5))

# ---------------------------------------------------------------------------------------------------------------------------------------
# Max Number Test
# ---------------------------------------------------------------------------------------------------------------------------------------

# class TestMaxNumber(unittest.TestCase):
# 	def test_highest_of_3(self):
# 		self.assertEqual(max_of_3(2, 8, 1), 8)
# 	def test_all_equal(self):
# 		self.assertEqual(max_of_3(8, 8, 8), 8)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Reverse String Test
# ---------------------------------------------------------------------------------------------------------------------------------------

# class TestReverseString(unittest.TestCase):
	
# 	def test_reverse(self):
# 		self.assertEqual(str_reverse("hello world"), "dlrow olleh")
		
# 	def test_reverse_caps(self):
# 		self.assertEqual(str_reverse("HELLO WORLD"), "DLROW OLLEH")
		
# 	def test_reverse_nums(self):
# 		self.assertEqual(str_reverse("12345"), "54321")
		
# 	def test_reverse_symbols(self):
# 		self.assertEqual(str_reverse("-_XxSnipezxX_-"), "-_XxzepinSxX_-")
		
# 	def test_reverse_int(self):
# 		self.assertEqual(str_reverse(123456789), "987654321")
		
# 	def test_reverse_flt(self):
# 		self.assertEqual(str_reverse(12.34567), "76543.21")
	
# 	def test_reverse_lst(self):
# 		self.assertEqual(str_reverse(["a","b","c","d","e"]), "edcba")

# ---------------------------------------------------------------------------------------------------------------------------------------
# String Word Count Test
# ---------------------------------------------------------------------------------------------------------------------------------------

# class TestCountString(unittest.TestCase):
# 	def test_nums(self):
# 		self.assertEqual(str_count("hello"), (0, 5, 0))

# 	def test_num_space(self):
# 		self.assertEqual(str_count("hello world"), (0, 10, 1))
# 		##Spaces count as characters

# 	def test_spaces(self):
# 		self.assertEqual(str_count("     "), (0, 0, 5))

# 	def test_symbols(self):
# 		self.assertEqual(str_count(",/.;'"), (0, 0, 5))

# 	def test_numbers(self):
# 		self.assertEqual(str_count("12345"), (0, 0, 5))

# 	def test_setence(self):
# 		self.assertEqual(str_count("This is a sentence."), (1, 14, 4))

# ---------------------------------------------------------------------------------------------------------------------------------------
# Factorial Test
# ---------------------------------------------------------------------------------------------------------------------------------------

# class TestFactorial(unittest.TestCase):
# 	def test_factorial(self):
# 		self.assertEqual(factorial_sum(3), 6)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Fibonacci Test
# ---------------------------------------------------------------------------------------------------------------------------------------

# class TestFibonacci(unittest.TestCase):
# 	def test_fibonacci(self):
# 		self.assertEqual(fibonacci_seq(7), 13)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Sum of a List Test
# ---------------------------------------------------------------------------------------------------------------------------------------

# class TestSumOfList(unittest.TestCase):
# 	def test_sum_of_list(self):
# 		self.assertEqual(sum_of_list([1,2,3,4]), 10)
# 	def test_multiple_list(self):
# 		self.assertEqual(sum_of_list([1,2,[3,4],[5,6]]), 21) #error
# if __name__ == '__main__':
# 	unittest.main()


# ---------------------------------------------------------------------------------------------------------------------------------------
# Int to String Test
# ---------------------------------------------------------------------------------------------------------------------------------------

class TestIntToStr(unittest.TestCase):
	def test_int_to_str(self):
		self.assertEqual(int_to_str(5),5)
if __name__ == '__main__':
	unittest.main()