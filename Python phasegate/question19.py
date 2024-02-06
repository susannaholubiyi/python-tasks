def check_factorial(number):
	if number in (0, 1):
		return 1
	if number < 0:
		return "invalid number"

	for count in range (number - 1, 0, -1):
		number *= count
		
	
	return number
	
number = int( input('enter number: '))
print(check_factorial(number))
