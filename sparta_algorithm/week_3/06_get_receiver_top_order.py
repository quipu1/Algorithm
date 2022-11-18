top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
	
	# 결과를 넣을 리스트 생성
	result = [0] * len(heights)
	
	for i in range(len(heights)):
		# 맨 오른쪽 탑부터 체크하기
		now_height = heights.pop()
		# 위에서 하나를 pop 해서 맨 오른쪽 탑의 위치인 index와 탑 개수의 값이 같아짐
		now = len(heights)
		# 리스트의 뒤에서 앞으로 출력
		for j in range(len(heights)-1, 0, -1):
			# 왼쪽에 있는 탑이 더 큰 게 나오면
			if now_height < heights[j]:
				# 더 큰 탑의 인덱스 값인 j+1을 넣는다
				result[now] = j + 1
				# 하나만 수신할 수 있으므로 break로 나와주기
				break
	return result


def get_receiver_top_orders(heights):
	answer = [0] * len(heights)

	while heights:
		height = heights.pop()
		for idx in range(len(heights)-1, 0, -1):
			if height[idx] > height:
				answer[len(heights)] = idx + 1
				break
	return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!