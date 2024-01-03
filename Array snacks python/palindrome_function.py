def palindrome(word):
	reversed_word = ''.join(reversed(word[0]))
	

	
	if word[0] == reversed_word:
		result = 'Is a palindrome'
	else:
		result = 'Is not a palindrome'
		
	return result


