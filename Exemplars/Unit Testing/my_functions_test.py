import unittest
from my_functions import *


class TestIsUpper(unittest.TestCase):
	def test_upper_true_minrange(self):
		self.assertTrue(isupper('A'))
	def test_upper_true_maxrange(self):
		self.assertTrue(isupper('Z'))
	def test_lower_false_minrange(self):
		self.assertFalse(isupper('a'))
	def test_lower_false_maxrange(self):
		self.assertFalse(isupper('z'))
	def test_nonalpha_false(self):
		self.assertFalse(isupper('@'))


class TestIsLower(unittest.TestCase):
	def test_lower_true_minrange(self):
		self.assertTrue(islower('a'))
	def test_lower_true_minrange(self):
		self.assertTrue(islower('z'))
	def test_upper_false_minrange(self):
		self.assertFalse(islower('A'))
	def test_upper_false_maxrange(self):
		self.assertFalse(islower('Z'))
	def test_nonalpha_false(self):
		self.assertFalse(islower('!'))


class TestCountUpperLowerIterative(unittest.TestCase):
	def test_3_upper_0_lower(self):
		self.assertEqual(count_upper_lower_iterative('ABC'), (3, 0))
	def test_3_lower_0_upper(self):
		self.assertEqual(count_upper_lower_iterative('xyz'), (0, 3))
	def test_1_upper_4_lower(self):
		self.assertEqual(count_upper_lower_iterative('Hello'), (1, 4))
	def test_2_upper_2_lower_2_nonalpha(self):
		self.assertEqual(count_upper_lower_iterative('W0rLd!'), (2, 2))
	def test_0_upper_0_lower(self):
		self.assertEqual(count_upper_lower_iterative(''), (0, 0))


class TestCountUpperLowerRecursive(unittest.TestCase):
	def test_3_upper_0_lower(self):
		self.assertEqual(count_upper_lower_recursive('ABC'), (3, 0))
	def test_3_lower_0_upper(self):
		self.assertEqual(count_upper_lower_recursive('xyz'), (0, 3))
	def test_1_upper_4_lower(self):
		self.assertEqual(count_upper_lower_recursive('Hello'), (1, 4))
	def test_2_upper_2_lower_2_nonalpha(self):
		self.assertEqual(count_upper_lower_recursive('W0rLd!'), (2, 2))
	def test_0_upper_0_lower(self):
		self.assertEqual(count_upper_lower_recursive(''), (0, 0))


class TestReverseStringShort(unittest.TestCase):
	def test_correct_reversal(self):
		self.assertEqual(reverse_str_short("Thomas"), "samohT")
	def test_incorrect_reversal(self):
		self.assertNotEqual(reverse_str_short("Connor"), "Connor")
	def test_integer(self):
		self.assertEqual(reverse_str_short(123), "321")


class TestReverseStringLong(unittest.TestCase):
	def test_correct_reversal(self):
		self.assertEqual(reverse_str_short("Thomas"), "samohT")
	def test_incorrect_reversal(self):
		self.assertNotEqual(reverse_str_short("Connor"), "Connor")
	def test_integer(self):
		self.assertEqual(reverse_str_short(123), "321")


class TestReverseStringRecursive(unittest.TestCase):
	def test_correct_reversal(self):
		self.assertEqual(reverse_str_recursive("Thomas"), "samohT")
	def test_incorrect_reversal(self):
		self.assertNotEqual(reverse_str_recursive("Connor"), "Connor")
	def test_integer(self):
		self.assertEqual(reverse_str_recursive(123), "321")
	def test_list(self):
		self.assertEqual(reverse_str_short([1,2,3]), "]3 ,2 ,1[")
	def test_dict(self):
		self.assertEqual(reverse_str_short({1:'a',2:'b',3:'C'}), "}'C' :3 ,'b' :2 ,'a' :1{")



class TestMaxNumber(unittest.TestCase):
	def test_highest_of_3(self):
		self.assertEqual(max_of_3(2, 8, 1), 8)
	def test_all_equal(self):
		self.assertEqual(max_of_3(5, 5, 5), 5)


class TestIsEven(unittest.TestCase):
	def test_even(self):
		self.assertTrue(is_even(10))
	def test_odd(self):
		self.assertFalse(is_even(5))


class TestSQRT(unittest.TestCase):
	def test_sqrt_4_2(self):
		self.assertEqual(sqrt(4), 2)
	def test_sqrt_9_3(self):
		self.assertEqual(sqrt(9), 3)
	def test_sqrt_float(self):
		self.assertIsNone(sqrt(3))


if __name__ == '__main__':
	unittest.main()