def convert_number_to_list(number):
	if number < 0:
		number *= -1
	
	new_array = [int(x) for x in str(number)]


	return new_array	
