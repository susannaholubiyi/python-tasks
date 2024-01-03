even_number = 0

odd_number = 0

for number in range (1,101):

	if number % 2 == 0:
		even_number += 1
	
	if number % 2 != 0:
		odd_number +=1
	
print('Number of Even numbers:', even_number, end=' ')
print('\nNumber of Odd numbers:', odd_number, end=' ')
