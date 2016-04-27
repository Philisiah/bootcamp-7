def data_type(x):
	'''
	Takes in an argument , x:
	- for integer , return x ** 2
	- for a float , return x * 2
	- for a string, returns "Hello" and that string
	- for boolean, returns "boolean"
	- for long returns, squareroot
	'''
	if type(x) == int:
		return x ** 2
	elif type(x) == float:
		return x / 2
	elif type(x) == str:
		return "Hello {}".format(x)
	elif type(x) == bool:
		return 'boolean'
	elif type(x) == long:
		return 'long'
	else:
		return x

print data_type(2)
print data_type(2.174)
print data_type('phil')
print data_type(True)
print data_type(2 ** 32)
