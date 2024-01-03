score = eval(input("Enter student scores or -1 to end: "))

passed = 0

fail = 0


while score != -1:

	if score  >= 45 and score < 100:
		passed +=1
		
	elif score < 45 and score >= 0:
		fail += 1
	elif score < 0 :
		print('Not a valid number')
	elif score > 100:
		print('Enter a valid score !')
		
	score = eval(input("Enter student scores or -1 to end: "))
		
	
print(f"Number of students that passed: ", passed)
print(f"Number of students that failed: ", fail)
