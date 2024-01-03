from concatenate_two_lists_function import concatenate_two_lists

def test_concatenate_two_lists():
	assert concatenate_two_lists([1, 2, 3, 4, 5], ['a', 'e', 'i', 'o', 'u']) == [ 1, 2, 3, 4, 5, 'a', 'e', 'i', 'o', 'u']
