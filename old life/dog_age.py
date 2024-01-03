dog_age = float(input("Enter a dog's age in human years: "))


if dog_age > 1 and dog_age <= 2:
	print(f"The dog's age in dog years = " , (dog_age * 10.5))
	

elif dog_age >2:
	print(f"The dog's age in dog years = " , (((dog_age - 2)* 4) +( 2 *10.5)))
