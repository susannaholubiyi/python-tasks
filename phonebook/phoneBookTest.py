import phoneBook
def test_get_contact_name():
    phoneBook.add_contact_name("joy")
    assert "joy" == phoneBook.get_contact_name(1)

def test_get_phone_number():
    phoneBook.add_phone_number("08033339112")
    assert "08033339112" == phoneBook.get_phone_number(1)



