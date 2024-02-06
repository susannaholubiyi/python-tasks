contacts = []


def add_contact(name, number):
    if number.isnumeric() :
        contact = {"name": name, "phone_number": number}
        contacts.append(contact)
        return "contact successfully added"
    else:
        return "Invalid number!"

def search_contact(name, number):
    contact_info = ""
    for contact in contacts:
        if contact["name"] == name and contact["phone_number"] == number:
            contact_info += contact["name"] + ": " + contact["phone_number"]

    if contact_info:
        return contact_info
    else: return "Contact not found!"

def delete_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)

def view_contacts():
    all_contacts = ""
    for contact in contacts:
       all_contacts +=  contact["name"] +": "  + contact ["phone_number"] + "\n"
    return all_contacts


def edit_contact(old_name, new_name, new_number):
    for contact in contacts:
        if contact["name"] == old_name:
            contact["name"] = new_name
            contact["phone_number"] = new_number








# def add_contact_name(name):
#     contact_names.append(name)

#
# def get_phone_number(index):
#     return phone_numbers[index - 1]
#
#
# def add_phone_number(phone_number):
#     phone_numbers.append(phone_number)
#
#
# def is_valid_number(phone_number):
#     if phone_number.isnumeric():
#         return True
#
#     return False
#
#
# def add_contact(name, phone_number):
#     contact_names.append(name)
#     phone_numbers.append(phone_number)
#
#
# def delete_contact(name):
#     # number_to_be_deleted = 0
#     for index in range(len(contact_names)):
#         if contact_names[index] == name:
#             print(name)
#             contact_names.pop(index)
#             phone_numbers.pop(index)
#
#
# def view_contact():
#     contacts = ""
#     for index in range(len(contact_names)):
#         #contacts += contact_names[index] + "    " + phone_numbers[index] + "\n"
#
#     return f"""contact_names[index] + " " + phone_numbers[index]"""



