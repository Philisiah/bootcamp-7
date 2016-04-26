def super_sum(A):
	'''takes a list of numbers(A)
	- double odd numbers
	- halves even numbers
	returns the sum'''
	add = 0
	
	for i in A:
		if i % 2 == 0:
			add = add + (i / 2)
			
		else:
			add = add + (i  * 2)
			
	return add