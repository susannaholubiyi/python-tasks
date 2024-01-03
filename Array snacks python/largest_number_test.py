from largest_number_function import largest_number

def test_largest_number_function():
	assert largest_number([1, 2, 3, 4, 5]) == 5
	assert largest_number([-1, -2, -3, -4, -5]) == -1
