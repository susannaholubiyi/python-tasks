import phone_book
from phone_book import contacts, add_contact, search_contact, delete_contact, view_contacts, edit_contact


class TestPhoneBook:

    # def __init__(self):
    #     self.contacts = contacts
    #     self.contacts.clear()

    def test_that_contact_can_saved(self):
        contacts.clear()
        add_contact("joy", "08109159434")
        assert len(contacts) == 1
        assert add_contact("chichi", "0902345678") == "contact successfully added"
        assert len(contacts) == 2
        contacts.clear()
    def test_that_invalid_contact_cannot_be_saved(self):
        contacts.clear()
        add_contact("joy", "0a$09159434")
        assert len(contacts) == 0
        contacts.clear()
    def test_that_valid_contact_cann_be_saved(self):
        contacts.clear()
        add_contact("joy", "0809159434")
        assert len(contacts) == 1
        contacts.clear()

    def test_that_a_none_existing_contact_cannot_be_gotten(self):
        contacts.clear()
        add_contact("joy", "08109159434")
        add_contact("chichi", "0902345678")
        add_contact("password", "89028")

        assert "Contact not found!" == search_contact("hf", "678")
        contacts.clear()
    def test_that_an_existing_contact_can_be_gotten(self):
        contacts.clear()
        add_contact("joy", "08109159434")
        add_contact("chichi", "0902345678")
        add_contact("password", "89028")

        contact_info = "joy: 08109159434"
        assert contact_info == search_contact("joy", "08109159434")
        contacts.clear()

    def test_that_existing_contact_can_be_deleted(self):
        contacts.clear()
        add_contact("joy", "08109159434")
        add_contact("sharon", "0902345678")
        add_contact("password", "89028")

        delete_contact("password")
        assert len(contacts) ==2
        contacts.clear()

    def test_that_none_existing_contact_cannot_be_deleted(self):
        contacts.clear()
        add_contact("joy", "08109159434")
        add_contact("sharon", "0902345678")
        add_contact("password", "89028")

        delete_contact("seun")
        assert len(contacts) ==3
        contacts.clear()

def test_view_contacts():
    contacts.clear()
    add_contact("joy", "08109159434")
    add_contact("sharon", "0902345678")

    assert view_contacts() == "joy: 08109159434\nsharon: 0902345678\n"
    contacts.clear()

def test_edit_existing_contact_name_only():
    contacts.clear()
    add_contact("joy", "08109159434")
    add_contact("sharon", "0902345678")
    assert search_contact("joy", "08109159434") == "joy: 08109159434"

    edit_contact("joy","Shalom","08109159434")
    assert search_contact("joy", "08109159434") == "Contact not found!"
    assert search_contact("Shalom", "08109159434") == "Shalom: 08109159434"




