array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
	result = []
	array1_idx = 0
	array2_idx = 0
	while len(result) != len(array1) + len(array2):
		if len(array1) == array1_idx:
			result.extend(array2[array2_idx:])
			return result
		elif len(array2) == array2_idx:
			result.extend(array1[array1_idx:])
			return result
		else:
			if array1[array1_idx] <= array2[array2_idx]:
				result.append(array1[array1_idx])
				array1_idx += 1
			elif array1[array1_idx] > array2[array2_idx]:
				result.append(array2[array2_idx])
				array2_idx += 1


# 강의
def merge(array1, array2):
	array_c = []
	array1_index = 0
	array2_index = 0

	while array1_index < len(array1) and array2_index < len(array2):
		if array1[array1_index] < array2[array2_index]:
			array_c.append(array1[array1_index])
			array1_index += 1
		else:
			array_c.append(array2[array2_index])
			array2_index += 1
	if array1_index == len(array1):
		while array2_index < len(array2):
			array_c.append(array2[array2_index])
			array2_index += 1

	if array2_index == len(array2):
		while array1_index < len(array1):
			array_c.append(array1[array1_index])
			array1_index += 1

	return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!