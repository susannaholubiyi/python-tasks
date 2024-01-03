number = int(input("Enter a list of  numbers to calculate the sum and average, input 0 to stop: "))

counter =0

sum = 0

while number != 0:

	counter+= 1
	
	sum += number
	
	number = int(input("Enter another number or 0 to stop: "))
	
print(f"Sum is " ,sum)
print(f"Average is", (sum/counter))
	
