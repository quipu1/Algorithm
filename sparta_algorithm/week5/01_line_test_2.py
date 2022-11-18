from collections import deque

c = 11
b = 2


# 최소시간 -> bfs
def catch_me(cony_loc, brown_loc):
	que = deque([])
	time = 0
	visited = [0] * 200001
	c = cony_loc

	que.append([brown_loc, time])

	while c <= 200000:

		c += time

		if visited[c]:
			return time

		for i in range(len(que)):
			q = que.popleft()
			b = q[0]

			if 0 <= b - 1 <= 200000 and visited[b - 1] == 0:
				que.append([b - 1, time+1])
				visited[b - 1] = 1
			if 0 <= b + 1 <= 200000 and visited[b + 1] == 0:
				que.append([b + 1, time+1])
				visited[b + 1] = 1
			if 0 <= 2 * b <= 200000 and visited[2 * b] == 0:
				que.append([2 * b, time+1])
				visited[2 * b] = 1

		time += 1

print(catch_me(c, b))  # 5가 나와야 합니다!
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10, 3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51, 50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550, 500))
