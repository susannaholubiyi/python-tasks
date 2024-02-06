sample_list = [10, 2, 8, 9, 3, 4, 1, 5]

def sort_list_in_ascending_order(sample_list):
	for index in range(len(sample_list)):
		for index2 in range(len(sample_list)):
			if sample_list[index] < sample_list[index2]:
				ascending = sample_list[index]
				sample_list[index] = sample_list[index2]
				sample_list[index2] = ascending
				
	return 	sample_list

numbers = [10, 2, 8, 9, 3, 4, 1, 5]	
print('Sample list in ascending order is', sort_list_in_ascending_order(numbers))

