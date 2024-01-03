from elements_on_even_position_function import elements_on_even_position
def test_elements_on_even_position():
	assert elements_on_even_position([1, 2, 3, 4, 5, 6, 7, 8, 9,]) == [2, 4, 6, 8]
	assert elements_on_even_position(['Seyi', 'Seun', 'Shalom', 'Sharon']) == ['Seun', 'Sharon']
