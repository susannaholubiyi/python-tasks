def running_total_of_a_list(elements):
	new_array = []
	sum = 0
	for index in range(len(elements)):
		sum += elements[index]
		new_array.append(sum)
		
	return new_array
