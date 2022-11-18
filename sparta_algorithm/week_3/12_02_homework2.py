def is_correct_parenthesis(string):
	stack = []
	for s in string:
		if s == '(':
			stack.append('(')
		elif len(stack) > 0 and s == ')':
			stack.pop()
		else:
			return False

	if len(stack) == 0:
		return True
	else:
		return False


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))