input = [4, 6, 2, 9, 1]


def selection_sort(array):
	for i in range(len(array)):
		min_val = array[i]
		min_idx = 0
		for j in range(i, len(array)):
			if array[j] <= min_val:
				min_val = array[j]
				min_idx = j
		array[i], array[min_idx] = min_val, array[i]

	return array


# 강의
def selection_sort(array):
	n = len(array)

	for i in range(n - 1):
		min_index = i
		for j in range(n - i):
			if array[i + j] < array[min_index]:
				min_index = i + j
		array[i], array[min_index] = array[min_index], array[i]

	return array

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!