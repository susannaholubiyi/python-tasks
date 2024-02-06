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





