import my_discount

def test_my_discount():
	assert my_discount.discount_applicator(150, 15) == 127.5
