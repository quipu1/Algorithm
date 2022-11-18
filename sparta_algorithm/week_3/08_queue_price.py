from collections import deque


def solution(prices):
	answer = []

	que = deque(prices)
	while que:
		now_price = que.popleft()
		cnt = 0
		for i in range(len(que)):
			if now_price <= que[i]:
				cnt += 1
			else:
				cnt += 1
				break
		answer.append(cnt)

	return answer

print(solution([1,2,3,2,3]))