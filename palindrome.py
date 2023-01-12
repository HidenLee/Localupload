def palindrome(text):
	text = text.replace(' ','')
	text = text.lower()
	return text == text[::-1] 

print(palindrome(input()))
