## 문자열 분리
def seperate_string(string):
	s_u = ""
	s_v = ""

	left = 0
	right = 0

	for i in range(len(string)):
		if string[i] == '(':
			left += 1
		else:
			right += 1

		if left == right:
			s_u = string[0:i + 1]
			s_v = string[i + 1:len(string)]
			break

	return s_u, s_v


# 올바른 괄호 판단
def collect(string):
	stack = []
	for s in string:
		if s == '(':
			stack.append('(')
		else:
			if len(stack) == 0:
				return False
			else:
				stack.pop()
	return True


# 뒤집기
def reverse_u(string):
	s = string[1:-1]
	return s[::-1]


# 총 집합
def get_correct_parentheses(balanced_parentheses_string):
	# 빈 문자열
	if balanced_parentheses_string == '':
		return ''

	# 문자열 분리
	u, v = seperate_string(balanced_parentheses_string)

	# 올바른 판단
	if collect(u):
		return u + get_correct_parentheses(v)
	else:
		return '(' + get_correct_parentheses(v) + ')' + reverse_u(u)


print(get_correct_parentheses("()))((()"))  # "()(())()"가 반환 되어야 합니다!
print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))
