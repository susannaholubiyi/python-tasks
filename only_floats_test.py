import only_floats_function

def test_only_floats_function():
	assert only_floats_function.only_floats(12.1, 23) == 1
	assert only_floats_function.only_floats(2, 3) == 0
	assert only_floats_function.only_floats(2.5, 5.5) == 2
