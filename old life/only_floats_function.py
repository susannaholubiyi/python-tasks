def only_floats(input_a, input_b):

	if input_a % 1 != 0 and input_b % 1 != 0:
		result = 2
	elif input_a % 1 == 0 and input_b % 1 != 0:
		result = 1
	elif input_a % 1 != 0 and input_b % 1 == 0:
		result = 1
	else:
		result = 0
		
	
	return result
