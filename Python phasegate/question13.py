def calculator (x, y):
	subtraction = x-y
	addition = x+y
	division = x / y
	multiplication = x * y
	remainder = x %y
	
	return subtraction, addition, division, multiplication, remainder
	
x = int(input('enter first number' ))
y = int(input('enter second number' ))
print (calculator(10, 20))
