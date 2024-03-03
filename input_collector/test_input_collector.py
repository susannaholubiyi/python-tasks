import input_collector


def test_get_length_of_list():
    assert 10 == input_collector.get_length_of_list(list_of_numbers=[3, 5, 7, 9, 11, 13, 15, 17, 19, 21])


def test_sum_elements_at_even_position():
    assert 65 == input_collector.sum_elements_at_even_position()


def test_sum_elements_at_odd_position():
    assert 55 == input_collector.sum_elements_at_odd_position()


def test_multiply_elements_at_every_third_position():
    assert 1729 == input_collector.multiply_elements_at_every_third_position()


def test_calculate_average_of_elemets_in_the_list():
    assert 12.1 == input_collector.calculate_average_of_elemets_in_the_list()


def test_get_largest_element_in_list():
    list_of_numbers = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    assert 21 == input_collector.get_largest_element_in_list(list_of_numbers)
    list_of_numbers2 = [3, 5, 7, 21, 11, 13, 15, 17, 19, 9]
    assert 21 == input_collector.get_largest_element_in_list(list_of_numbers2)


def test_get_smallest_element_in_list():
    assert 3 == input_collector.get_smallest_element_in_list()


def test_check_first_and_last_character_in_string():
    list_of_names = ['Seyi', 'dad', 'seun']
    assert ['dad'] == input_collector.check_first_and_last_character_in_string(list_of_names)
    list_of_names2 = ['mum', 'dad', 'seun']
    assert ['mum','dad'] == input_collector.check_first_and_last_character_in_string(list_of_names2)
