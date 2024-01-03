from palindrome_function import palindrome

def test_palindrome():

	assert palindrome(['abba']) == 'Is a palindrome'
	assert palindrome(['Susannah']) == 'Is not a palindrome'
	assert palindrome(['101']) == 'Is a palindrome'	
