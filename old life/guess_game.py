from random import randint

random_number = randint(1,10)


number_of_guess = 1
while number_of_guess <= 3:

	guess_number = int(input("Guess a number from 1-10: "))

	if guess_number== random_number:
	
		print("You've won!")
		break
		
	elif guess_number != random_number:
	
		print("So close, try again!")

		
	if guess_number > 10 and guess_number < 1:

		print("Enter a number from 1-10")
	
	number_of_guess +=1
		
		
