from reverse_list_function import reverse_list

def test_reverse_list():
	assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
	assert reverse_list(['a', 'b', 'c', 'd', 'e']) == ['e', 'd', 'c', 'b', 'a']
