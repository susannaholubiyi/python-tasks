def get_fibonacci_series():
	series_counter = 0
	previous_sum = 0
	sum = 1
	print(0, 1, end=" ")
	for number in range(10):
		previous = sum
		sum += series_counter
		print(sum, end=" ")
		series_counter = previous

get_fibonacci_series()		
