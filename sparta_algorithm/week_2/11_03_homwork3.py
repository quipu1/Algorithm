numbers = [1, 1, 1, 1, 1]
target_number = 3
result = []


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, now_idx, now_sum, all_ways):

	if now_idx == len(array):
		all_ways.append(now_sum)
		return

	get_count_of_ways_to_target_by_doing_plus_or_minus(array, now_idx + 1, now_sum + array[now_idx], all_ways)
	get_count_of_ways_to_target_by_doing_plus_or_minus(array, now_idx + 1, now_sum - array[now_idx], all_ways)


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, 0, 0, result)
print(result.count(target_number))
