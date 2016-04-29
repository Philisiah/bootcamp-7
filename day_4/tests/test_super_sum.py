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
		self.assertEqual(super_sum(-1, 1), 0)
		self.assertNotEqual(super_sum(10, 20, 30), 100)

	def test_single_list(self):
		'''test sum of items in a list'''
		self.assertEqual(super_sum([1, 2, 3]), 6)

	def test_for_string(self):
		'''
		tests for string input
		'''
		self.assertEqual(super_sum('string', 1, 4), 0)

if __name__ == '__main__':
	unittest.main()