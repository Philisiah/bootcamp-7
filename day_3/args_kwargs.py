def Hello(name, age, class_=''):
	'''
	'''
	if class_ != '':
		return "I am {}, and i am {} years old and {} class".format(name, age, class_)

	return "I am {}, and i am {} years old".format(name, age)

people = [("jane", 25, 'High'),
("James", 27, 'Low'),
("Micheal", 63),
("Gary", 54)]
'''for i, j in people:
	print i
	print j
	print Hello(i, j)'''
for person in people:
	print Hello(*person)

def super_sum1(*args, **kwargs):
	'''
	returns the sum 
	'''
	sum2 = 0
	for i in args:
		sum2 += i
	return sum2
n = (2,5,45,23)
print super_sum1(*n)
print super_sum1(2,5,45,23)

def hello_again(**kwargs):
	return "I am {}, and i am {} years old".format(kwargs['name'], kwargs['age'])

joe = {'name':'joe', 'age':63}
print hello_again(**joe)
print hello_again(name="jane", age=25 )

other_people = [
{'name': 'Phil', 'age':79},
{'name':'Gary', 'age': 36}
]
for i in other_people:
	print hello_again(**i)
#print hello_again(**other_people)