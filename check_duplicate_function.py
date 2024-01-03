def check_duplicates(list_of_things):

	single = set()
	duplicate = set()
	
	for thing in list_of_things:
		if thing in single:
			duplicate.add(thing)
		else:
			single.add(thing)
	
	if duplicate:
		return list(duplicate)
	else:
		return 'no duplicates'
		
		
	
