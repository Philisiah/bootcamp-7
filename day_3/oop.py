# instance vs class variable
# class methods
from person import Person
from kenyan import Kenyan

p1 = Person('Joe', 23)
p2 = Person('Jane', 23)
p3 = Person('George', 35)
print p3.say_hello()
print p2.people_count
print Person.people_count

b = []
a = [('phil', 23), ('jane', 23), ("jane", 25),
     ("James", 27), ("Micheal", 63), ("Gary", 54)]
for name, age in a:
    person = Person(name, age)
    b.append(person)
print b

k = Kenyan('Anne Waiguru', 50)
k.probe(True)
print "Is {}, corrupt? {}".format(k.name, k.is_corrupt())
print k.say_hello()
