first_number = int(input('enter first number: '))

second_number = int(input('enter second number: '))

third_number = int(input('enter third number: '))


total = first_number + second_number + third_number
max = first_number
if max < second_number:
	max = second_number

elif max < third_number:
	max = third_number

print("The total is", total)
print("The largest number is", max)
