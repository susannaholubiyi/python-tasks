from check_if_key_is_present_function import check_if_key_is_present

def test_check_if_key_is_present():
	assert check_if_key_is_present([10, 2, 8, 9, 3, 4, 1, 5], 12) == "12 is not present"
	assert check_if_key_is_present([10, 2, 8, 9, 3, 4, 1, 5], 3) == "3 is present and located at index 4"
