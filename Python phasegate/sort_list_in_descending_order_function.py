def sort_list_in_descending_order(sample_list):
	for index in range(len(sample_list)):
		for index2 in range(len(sample_list)):
			if sample_list[index] > sample_list[index2]:
				descending = sample_list[index]
				sample_list[index] = sample_list[index2]
				sample_list[index2] = descending
			
	return sample_list

numbers = [10, 2, 8, 9, 3, 4, 1, 5]	
print('Sample list in descending order is', sort_list_in_descending_order(numbers) )
