from combine_two_lists_function import combine_two_lists

def test_combine_two_lists():

	assert combine_two_lists(['a', 'e', 'i', 'o', 'u'], [1, 2, 3, 4, 5]) == ['a', 1, 'e', 2, 'i', 3, 'o', 4, 'u', 5]
	assert combine_two_lists(['A', 'B', 'C'], [1, 2, 3, 4, 5]) == ['A', 1, 'B', 2, 'C', 3, 4, 5]
	assert combine_two_lists(['A', 'B', 'C', 'D', 'E', 'F', 'G'], [1, 2, 3]) == ['A', 1, 'B', 2, 'C', 3, 'D', 'E', 'F', 'G']	
