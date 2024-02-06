def alphabet_checker (alphabet):
	if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u' or alphabet == 'A' or alphabet == 'E' or alphabet == 'I' or alphabet == 'O' or alphabet == 'U':
		answer = vowel
		
	else:
		answer = consonant
		
	return answer

alphabet = input("Enter alphabet to check if it is a vowel or not: ")
print(alphabet_checker(alphabet))
		
