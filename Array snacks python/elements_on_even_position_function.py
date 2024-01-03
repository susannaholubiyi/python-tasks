def elements_on_even_position(elements):
	
	new_array = []
	for index in range(len(elements)):
		if index % 2 != 0:
			new_array .append(elements[index])
	return new_array
