def funky(a, b):
	if isinstance(a,  (int, float, str, list)) and isinstance(b, (int, float, str, list)):
		return a + b
	elif isinstance(a, dict) and isinstance(b, dict):
		z = dict(a.items() + b.items())
		return z
	else:
		return "NO CAN DO"


		

print funky(3.67, 3.5)
print funky(5,6)
print funky('5', '6')
print funky([2, 45], [25, 36,78])
fellow = {1:'mary', 2:'pauline'}
dad = {'name': 'Fischer', 'age': 42}
print funky(fellow, dad)
print funky({1:'mary', 2:'pauline', 4:'bary'}, {'name': 'Fischer', 'age': 42, 'home':'taita'})

