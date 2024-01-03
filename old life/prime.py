for number in range (1,101):

counter = 0

factor_counter = 0

while counter <= number:

	if number % counter == 0:
		factor_counter += 1
		counter += 1
		
	elif number % counter != 0:
		counter +=1
		
	


