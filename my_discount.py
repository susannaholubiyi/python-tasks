def discount_applicator(price, discount):

	percentage_discount = discount / 100

	new_price = price - ( price * percentage_discount )

	return new_price
