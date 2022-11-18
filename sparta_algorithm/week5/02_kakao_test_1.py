from collections import deque

input = "abcabcabcabcdededededede"


def string_compression(string):

	# 문자열을 자르는 단위
	max_cut = 1
	result = []

	while max_cut < len(string):

		# 이 전의 문자열 담을 곳
		last_string = string[0:max_cut]
		length = max_cut
		same = 0


		for i in range(max_cut, len(string), max_cut):

			# 남은 문자열 수가 자르는 단위 보다 적을 때
			if len(string) - i < max_cut:
				length += len(string) - i
				break

			# 이전의 문자열과 같을 때
			if last_string == string[i:i+max_cut]:
				if same == 0:
					length += 1
					same += 1

			# 이전의 문자열과 다를 때
			else:
				length += max_cut
				last_string = string[i:i+max_cut]
				same = 0

		result.append(length)
		max_cut += 1

	return min(result)


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))