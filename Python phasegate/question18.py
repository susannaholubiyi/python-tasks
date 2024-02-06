#def discount_getter(item_bougth):
item_bought = input("What do you want to buy? ")
if item_bought == 'electronics':
	print('Discount is 10%')
	price_of_electronics = float(input("Enter the price of the electronic you want to buy: "))
	discount_for_electronic = price_of_electronics * 0.1
	print("You get a discount of", discount_for_electronic)
	print("You are to pay", (price_of_electronics - discount_for_electronic))

elif item_bought == 'clothing':
	print('Discount is 15%')
	price_of_clothing = float(input("Enter the price of the clothing you want to buy: "))
	discount_price_for_clothing = price_of_clothing * 0.15
	print ("You get a discount of", discount_price_for_clothing)
	print("You are to pay", (price_of_clothing - discount_price_for_clothing))

else:
	print('There is no discount')
	price_of_other = float(input("Enter the price of the other products you want to buy: "))
	print("You are to pay", price_of_other)
	

	
	

	
	
