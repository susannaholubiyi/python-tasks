from element_occur_in_list_function import element_occur_in_list

def test_element_occur_in_list():
	assert element_occur_in_list([1, 2, 3, 4, 5], 100) == 'no'
	assert element_occur_in_list(['a', 'b', 'c', 'd', 'e'], 'a') == 'yes'
