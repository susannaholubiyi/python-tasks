from sort_list_in_ascending_order_function import sort_list_in_ascending_order

def test_sort_list_in_ascending_order():
	assert sort_list_in_ascending_order([10, 2, 8, 9, 3, 4, 1, 5]) == [1, 2, 3, 4, 5, 8, 9, 10]
	assert sort_list_in_ascending_order([10, -2, 8, -20, 3, 0, 1, 5]) == [-20, -2, 0, 1, 3, 5, 8, 10]
