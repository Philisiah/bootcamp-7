#instance vs class variable
#class methods
class Person:
	people_count = 0
	def __init__(self, name, age=0):
		self.name = name
		if age!=0:
			self.age = age
		Person.people_count += 1

	def __repr__(self):
		return "<object: {}, {}>".format(self.name, self.age)
	def say_hello(self):
		return "Hello, I'm {} age and {} y/o".format(self.name, self.age)


		
p1 = Person('Joe', 23)
p2 = Person('Jane', 23)
p3 = Person('George', 35)
print p3.say_hello()
print p2.people_count
print Person.people_count

b = []
a = [('phil', 23), ('jane', 23), ("jane", 25), ("James", 27), ("Micheal", 63), ("Gary", 54)]
for name, age in a:
	person = Person(name, age)
	b.append(person)
print b

