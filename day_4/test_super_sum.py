import unittest
from super_sum import super_sum

class SuperSumTestCase(unittest.TestCase):
	''' TestCase for supersum'''
	def test_empty_input(self):
		'''test empty input '''
		self.assertEqual(super_sum(), "Please enter numbers" )

	def test_sum_of_integers(self):
		'''test test_sum_of_integers'''
		self.assertEqual(super_sum(1, 2, 3), 6)