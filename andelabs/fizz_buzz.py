def fizz_buzz(number):
	''' function fizz_buzz that evaluates numbers 
	'''
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number

print fizz_buzz(3)
print fizz_buzz(15)
print fizz_buzz(20)
print fizz_buzz(7)
