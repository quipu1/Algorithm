input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
	result = 0

	for i in array:
		if i <= 1 or result <= 1:
			result += i
		else:
			result *= i

	return result


result = find_max_plus_or_multiply(input)
print(result)

# 강의
def find_max_plus_or_multiply(array):
	multiply_sum = 0

	for number in array:
		if number <= 1 or multiply_sum <= 1:
			multiply_sum += number
		else:
			multiply_sum *= number

	return result