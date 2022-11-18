from collections import deque

balanced_parentheses_string = "()))((()"



def get_correct_parentheses(balanced_parentheses_string):
	u = ""
	v = ""

	left = 0
	right = 0

	# 1~2
	for i in range(len(balanced_parentheses_string)):
		if balanced_parentheses_string[i] == '(':
			left += 1
		elif balanced_parentheses_string[i] == ')':
			right += 1

		if left == right:
			u = balanced_parentheses_string[0:i + 1]
			v = balanced_parentheses_string[i + 1:len(balanced_parentheses_string)]
			break

	# 3
	correct = 0
	stack = []
	for uu in u:
		if uu == "(":
			stack.append(uu)
		else:
			if len(stack) == 0:
				correct = 1
			else:
				stack.pop()

	if correct == 1:
		return get_correct_parentheses(v)

	# 탈출 조건
	if len(balanced_parentheses_string) <= 0:
		return ""

	# 4
	if correct == 0:
		new = "("
		new += get_correct_parentheses(v)
		new += ")"
		new += u[len(u)-1:1:-1]
		return new






print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))