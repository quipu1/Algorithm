input = "abcba"

def is_palindrome(string):
	if string == string[::-1]:
		return True
	else:
		return False


# 강의
def is_palindrome(string):
	n = len(string)
	for i in range(len(string)):
		if string[i] != string[n-1-i]:
			return False
	return True


def is_palindrome(string):
	if len(string) <= 1:
		return True
	if string[0] == string[-1]:
		return is_palindrome(string[1:-1])
	else:
		return False


# 강의
def is_palindrome(string):
	if len(string) <= 1:
		return True

	if string[0] != string[-1]:
		return False

	return is_palindrome(string[1:-1])


print(is_palindrome(input))