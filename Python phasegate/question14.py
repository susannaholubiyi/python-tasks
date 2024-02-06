def is_prime(number):
	counter = 0
	factor_counter = 0
	for counter in range(1, (number +1)):
		if number % counter == 0:
			factor_counter += 1
			counter += 1
	if factor_counter == 2:
		return True
	else:
		return False
	


print(is_prime(7))
print(is_prime(2))
