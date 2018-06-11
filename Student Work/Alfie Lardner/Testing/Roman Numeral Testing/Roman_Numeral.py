import unittest
from roman_function import * 

class RomanNumeral(unittest.TestCase):

	def test_hundred(self):
		self.assertEqual(get_roman(100), 'C')

	def test_thousand(self):
		self.assertEqual(get_roman(1000), 'M')

if __name__ == '__main__':
	unittest.main()
