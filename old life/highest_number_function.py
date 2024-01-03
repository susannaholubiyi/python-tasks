def highest_number (number1, number2, number3):

	if number1 > number2 and number1 > number3:
		result = number1
	if number2 > number1 and number2 > number3:
		result = number2
	if number3 > number1 and number3 > number2:
		result = number3
		
	return result

print(highest_number(5,7,9))
