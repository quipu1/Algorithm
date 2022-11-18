numbers = [1, 1, 1, 1, 1]
target_number = 3
all_case = []


# 모든 케이스의 계산을 다 해봐야함
def get_all_case(arr, idx, sum_arr):

	# numbers의 마지막 요소까지 계산을 했다면 결과값 넣어주기
	if len(arr) == idx:
		return all_case.append(sum_arr)

	get_all_case(arr, idx + 1, sum_arr + arr[idx])
	get_all_case(arr, idx + 1, sum_arr - arr[idx])


get_all_case(numbers, 0, 0)
print(all_case.count(target_number))

