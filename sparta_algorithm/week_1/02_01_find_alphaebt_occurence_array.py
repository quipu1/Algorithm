def find_alphabet_occurrence_array(string):
	alphabet_occurrence_array = [0] * 26

	for s in string:
		if s.isalpha():
			alphabet_occurrence_array[ord(s) - 97] += 1

	max_index_alpha = alphabet_occurrence_array.index(max(alphabet_occurrence_array))
	result = chr(max_index_alpha + 97)

	return result


print(find_alphabet_occurrence_array("hello my name is sparta"))


# 강의
def find_alphabet_occurrence_array_one(string):
	alphabet_occurrence_array = [0] * 26

	for char in string:
		if not char.isalpha():
			continue
		arr_index = ord(char) - ord("a")
		alphabet_occurrence_array[arr_index] += 1

	return alphabet_occurrence_array
