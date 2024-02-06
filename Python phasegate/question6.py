def is_palindrome(word):
	if word == word[::-1]:
		return True
	else:
		return False

word = input("Enter word to check if it's a palindrome: ")
print(is_palindrome(word))
