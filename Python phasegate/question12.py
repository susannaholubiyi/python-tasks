def square_of_number():
	list_of_numbers = []

	for number in range (1, 26):
		list_of_numbers.append(number ** 2)
	return list_of_numbers 
print(square_of_number())
