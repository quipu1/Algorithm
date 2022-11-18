def find_alphabet_occurrence_array(string):
	alphabet_occurrence_array = [0] * 26


	for s in string:
		if s.isalpha():
			alphabet_occurrence_array[ord(s) - 97] += 1

	m_alpha = max(alphabet_occurrence_array)
	cnt = alphabet_occurrence_array.count(m_alpha)

	if cnt > 1:
		result = []
		for i in range(len(alphabet_occurrence_array)):
			if m_alpha == alphabet_occurrence_array[i]:
				result.append(chr(i + ord("a")))
		return ' '.join(result)

	else:
		max_index_alpha = alphabet_occurrence_array.index(m_alpha)
		result = chr(max_index_alpha + ord("a"))
		return result


print(find_alphabet_occurrence_array("MMM"))
