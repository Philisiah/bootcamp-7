def super_sum(*args):
	'''
	returns the sum of numbers.
	e.g.
	super_sum() ==> Please enter numbers 
	super_sum(1, 2, 3) ===> 6
	super_sum([10], [20], [30]) ==> 60
	super_sum([1, 2, 3]) ==> 6
	'''
	if not args:
		return  "Please enter numbers"
	for arg in args:
		total = 0
		if type(arg) == int:
			total += arg
	return total