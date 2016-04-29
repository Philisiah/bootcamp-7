def super_sum(*args):
	'''
	returns the sum of numbers.
	e.g.
	super_sum() ==> Please enter numbers 
	super_sum(1, 2, 3) ===> 6
	super_sum([10], [20, 30]) ==> 60
	super_sum([1, 2, 3]) ==> 6
	super_sum("string") ==> 0
	'''
	total = 0
	if args:
		for x in args:
			if type(x) == list:
				for i in x:
					total += i
			elif type(x) == str:
				return 0
			else:
				total += x 
		return total
	return  "Please enter numbers"
	
