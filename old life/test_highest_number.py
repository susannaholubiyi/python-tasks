import highest_number_function

def test_highest_number_function():
	assert highest_number_function.highest_number(3, 5, 9) == 9
	
	assert highest_number_function.highest_number(6, 4, 1) == 6
	
	assert highest_number_function.highest_number(3, 4, 11) == 11
