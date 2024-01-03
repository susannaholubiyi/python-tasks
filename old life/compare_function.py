def highest_number (a=1, b=2, c=3):

	if a > b and a > c:
		return a
	if b > a and b> c:
		return b
	if c > a and c > b:
		return c

print(highest_number(5,9,50))
