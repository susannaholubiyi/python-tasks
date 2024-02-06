def sum_of_odd():
	sum = 0;
	for number in range (1,51):
		if number % 2 != 0:
			sum += number
	return sum

print (sum_of_odd())

