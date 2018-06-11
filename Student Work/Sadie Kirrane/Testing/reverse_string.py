import unittest
from my_functions import *

class TestReverseString(unittest.TestCase):

	def test_correct_reversal(self):
		self.assertEqual(reverse_str("Sadie"), "eidaS")

	def test_incorrect_reversal(self):
		self.assertNotEqual(reverse_str("Max"), "xaM")
