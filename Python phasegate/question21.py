def reverse_string(name):
	length_of_name = len(name) - 1
	reversed_name = ""
	for num in range(length_of_name, -1, -1):
		reversed_name += name[num]
	return reversed_name

print(reverse_string("Susannah"))
