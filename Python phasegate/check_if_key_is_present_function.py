
def check_if_key_is_present(sample_list, key):
	for index in range(len(sample_list)):
		if key == sample_list[index]:
			return f"{key} is present and located at index {index}"
		
	return f"{key} is not present"

sample_list = [10, 2, 8, 9, 3, 4, 1, 5]
key = 12
print(check_if_key_is_present(sample_list, key))
