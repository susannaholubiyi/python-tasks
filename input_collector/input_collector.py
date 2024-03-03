list_of_numbers = []
number = 1
for index in range (10):
    number+=2
    list_of_numbers.append(number)

print(list_of_numbers)

def get_length_of_list(list_of_numbers):
    length = 0
    for index in list_of_numbers:
        length+=1
    return length

def sum_elements_at_even_position():
    sum_of_even_position_element = 0
    for index in range (len(list_of_numbers)):
        if index % 2 != 0:
            sum_of_even_position_element += list_of_numbers[index]
    return sum_of_even_position_element

def sum_elements_at_odd_position():
    sum_of_odd_position_element = 0
    for index in range (len(list_of_numbers)):
        if index % 2 == 0:
            sum_of_odd_position_element += list_of_numbers[index]

    return sum_of_odd_position_element

def multiply_elements_at_every_third_position():
    third_positions_multiplication = 1
    for index in range(2,len(list_of_numbers),3):
        third_positions_multiplication *= list_of_numbers[index]

    return third_positions_multiplication

def calculate_average_of_elemets_in_the_list():
    average = 0
    sum = 1
    for index in range(len(list_of_numbers)):
        sum += list_of_numbers[index]
        average = sum / len(list_of_numbers)

    return average

def get_largest_element_in_list(list_of_numbers):
    largest_element = list_of_numbers[0]
    for index in range(len(list_of_numbers)):
        if list_of_numbers[index] > largest_element:
            largest_element = list_of_numbers[index]

    return largest_element

def get_smallest_element_in_list():
    smallest_number = list_of_numbers[0]
    for index in range(len(list_of_numbers)):
        if list_of_numbers[index] < smallest_number:
            smallest_number = list_of_numbers[index]

    return smallest_number


def check_first_and_last_character_in_string(list_of_names):
    show_name = []
    for name in list_of_names:
        if len(name) >= 2:
            if name[0]==name[-1]:
                show_name.append(name)

    return show_name

