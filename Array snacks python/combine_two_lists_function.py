def combine_two_lists(letters, numbers):

	new_array = []
	count1 = 0
	count2 = 0
	
	while count1 < len(letters) and count2 < len(numbers):
		new_array.append(letters[count1])
		new_array.append(numbers[count2])
		
		count1 += 1
		count2 += 1
		
	while count1 < len(letters):
		new_array.append(letters[count1])
		count1 += 1
	
	while count2 < len(numbers):
		new_array.append(numbers[count2])
		count2 += 1

	return new_array
	
