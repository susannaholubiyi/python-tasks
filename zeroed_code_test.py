from zeroed_code_function import zeroed_code

def test_zeroed_code_function():

	assert zeroed_code([10, 20, 30, 40, 50]) == [0, 20, 30, 40, 0]
