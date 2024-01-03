def element_occur_in_list(elements, element):
	index = 0
	while index < len(elements):
		if element in elements:
			answer = 'yes'
		else:
			answer = 'no'
		index += 1
		
	return answer
	
