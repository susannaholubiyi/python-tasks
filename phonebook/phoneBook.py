contact_names = []
phone_numbers = []


def get_contact_name(index):
    return contact_names[index -1]
def add_contact_name(name):
    contact_names.append(name)
def get_phone_number(index):
    return phone_numbers[index-1]
def add_phone_number(phone_number):
    phone_numbers.append(phone_number)
def is_valid_number(phone_number):
    if phone_number.isnumeric():
        return True

    return False

