def largest_number(numbers):
	max = numbers[0]
	index = 0

	while index < len(numbers):
		if numbers[index] > max:
			max = numbers[index]
		index += 1
		
	return  max
