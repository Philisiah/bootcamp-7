from exporter import super_sum, hello_again, max_min, people
'''imports classes  and variables into the function
'''
print super_sum, hello_again, max_min, people

a = [10, 20, -5, 6, 50, 8]

print max_min(a)

print super_sum(*a)

print hello_again('Joe', 23)

print hello_again(*people[0])
gap