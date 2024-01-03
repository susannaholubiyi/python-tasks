from check_duplicate_function import check_duplicates

def test_check_duplicate():
	assert check_duplicates(['apple', 'orange', 'banana', 'apple']) == ['apple']
	assert check_duplicates(['Yoda', 'Moses', 'Joshua', 'Mark']) == 'no duplicates'
