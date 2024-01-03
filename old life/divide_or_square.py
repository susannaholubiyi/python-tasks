def divide_or_square(number):

	number = eval(input("Enter any number: "))

	if number % 5 == 0:
		result = number ** 0.5

	
	elif number % 5 != 0:
		result = number - ((number // 5) * 5)



		
	return result




