input = [3, 5, 6, 1, 2, 4]


# 내 코드
def find_max_num(array):
	max_num = array[0]
	for a in array:
		if a > max_num:
			max_num = a
	return max_num


result = find_max_num(input)
print(result)


# 강의 답안 1
def find_max_num_one(array):
	for num in array:
		for compare_num in array:
			if num < compare_num:
				break
			else:
				return num

# 강의 답안 2
def find_max_num_two(array):
	max_num = array[0]
	for num in array:
		if num > max_num:
			max_num = num
	return max_num
