input = "hello my name is sparta"


# 강의 1
def find_max_occurred_alphabet(string):
	alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
	                  "t", "u", "v", "x", "y", "z"]

	max_occurrence = 0
	max_alphabet = alphabet_array[0]

	for alphabet in alphabet_array:
		occurrence = 0
		for char in string:
			if char == alphabet:
				occurrence += 1

		if occurrence > max_occurrence:
			max_occurrence = occurrence
		max_alphabet = alphabet

	return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)


# 강의 2
def find_max_occurred_alphabet_two(string):
	alphabet_occurrence_array = [0] * 26

	for char in string:
		if not char.isalpha():
			continue
		arr_index = ord(char) - ord("a")
		alphabet_occurrence_array[arr_index] += 1

	max_occurrence = 0
	max_alphabet_index = 0
	for index in range(len(alphabet_occurrence_array)):
		alphabet_occurrence = alphabet_occurrence_array[index]

		if alphabet_occurrence > max_occurrence:
			max_alphabet_index = index
			max_occurrence = alphabet_occurrence

	return chr(max_alphabet_index + ord("a"))