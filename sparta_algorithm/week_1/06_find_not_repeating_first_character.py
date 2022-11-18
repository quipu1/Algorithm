input = "abadabac"


def find_not_repeating_character(string):
	alphabet = [0] * 26
	repeat = []

	for s in string:
		if not s.isalpha():
			continue
		alphabet[ord(s) - ord("a")] += 1


	for i in range(len(alphabet)):
		if alphabet[i] == 1:
			repeat.append(chr(i + ord("a")))

	for s in string:
		if s in repeat:
			return s


result = find_not_repeating_character(input)
print(result)


# 강의
def find_not_repeating_character(string):
	alphabet_occurrence_array = [0] * 26

	for char in string:
		if not char.isalpha():
			continue
		arr_index = ord(char) - ord("a")
		alphabet_occurrence_array[arr_index] += 1

	not_repeating_character_array = []
	for index in range(len(alphabet_occurrence_array)):
		alphabet_occurrence = alphabet_occurrence_array[index]
		if alphabet_occurrence == 1:
			not_repeating_character_array.append(chr(index + ord("a")))

	for char in string:
		if char in not_repeating_character_array:
			return char