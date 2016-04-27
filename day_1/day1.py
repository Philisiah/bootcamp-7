def add(a, b):
	'''
	print sum of two numbers
    '''

    if type(a) and type(b) == int:
        return a + b
    elif type(a) and type(b) == list:
        return a + b
    elif type(a) and type(b) == str:
        return a + b
    elif type(a) and type(b) == float:
        return a + b
    elif type(a) == str or type(b) == else:
        return 'NUMBER HAS TO BE AN INT!'

print add(3.67, 3.5)
#add('phil', 34)
print add(5, 6)
print add('5', '6')
print add([5], [45])
