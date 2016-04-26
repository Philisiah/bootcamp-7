def funky(a, b):
	if isinstance(a,  (int, float, str, list)) and isinstance(b, (int, float, str, list)):
		return a + b
	elif isinstance(a, dict) and isinstance(b, dict):
		z = dict(a.items() + b.items())
		return z
	else:
		return "NO CAN DO"