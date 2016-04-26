def sum_digits(A):
	'''
	Takes in a list A and returns 
	the sum of all the digits in the list.
	e.g. [10, 30, 45] should return 
	1 + 0 + 3 + 0 + 4 + 5 = 13
	'''
	total = 0
	for i in A:
		a = str(i)
		for x in a:
			total += int(x)
	return total