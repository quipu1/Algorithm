input = "001100"

# 모두 0으로 바꿀거다
#   1  0  1  1  0  1  1  1  0  1
# 1   0  1     0  1        0  1
#
# 1=>0으로 바뀌는 횟수가 더 적으면 1로 만드는 것이 좋다.
# 0=>1으로 바뀌는 횟수가 더 적으면 0으로 만드는 것이 좋다.
#
# 모두 0으로 바꾸려면 걸리는 횟수 => 4
# 모두 1로 바꾸려면 걸리는 횟수 => 3


def find_count_to_turn_out_to_all_zero_or_all_one(string):
	# 0에서 1로 바뀌는 횟수 / 1에서 0으로 바뀌는 횟수
	to_one = 0
	to_zero = 0

	now = string[0]
	if string[0] == "0":
		to_zero += 1
	elif string[0] == "1":
		to_one += 1

	for i in range(1, len(string)):
		if now[-1] != string[i]:
			if string[i] == "0":
				to_zero += 1
			elif string[i] == "1":
				to_one += 1
		now += string[i]

	if to_zero <= to_one:
		return to_zero
	else:
		return to_one



result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

def find_count_to_turn_out_to_all_zero_or_all_one(string):
	count_to_all_zero = 0
	count_to_all_one = 0

	if string[0] == '0':
		count_to_all_one += 1
	elif string[0] == '1':
		count_to_all_zero += 1

	for i in range(len(string)-1):
		if string[i] != string[i+1]:
			if string[i+1] == '0':
				count_to_all_one += 1
			if string[i+1] == '1':
				count_to_all_zero += 1

	return min(count_to_all_one, count_to_all_zero)