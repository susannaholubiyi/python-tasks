def sum_of_elements_in_a_list(elements):
	

	sum = 0
	
	for index in range(0, len(elements)):
		sum += elements[index]
		
	return sum
	
	sum = 0
	index = 0
	while index < len(elements):
		sum += elements[index]
		index += 1
	return sum
