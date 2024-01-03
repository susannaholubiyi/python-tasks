from elements_on_odd_position_function import elements_on_odd_position
def test_elements_on_odd_position():
	assert elements_on_odd_position([1, 2, 3, 4, 5, 6, 7, 8, 9,]) == [1, 3, 5, 7, 9]
	assert elements_on_odd_position(['Seyi', 'Seun', 'Shalom', 'Sharon']) == ['Seyi', 'Shalom']
