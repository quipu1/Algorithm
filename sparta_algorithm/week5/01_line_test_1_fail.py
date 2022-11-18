from collections import deque

c = 11
b = 2


# 최소시간 -> bfs
def catch_me(cony_loc, brown_loc):
	que = deque([])
	time = 0
	flag = 1
	visited = [0] * 200001

	que.append([cony_loc, brown_loc, time])

	while flag:

		for i in range(len(que)):
			q = que.popleft()

			c = q[0]
			b = q[1]
			t = q[2]

			t += 1
			now_c = c + t

			if now_c > 20000 or now_c == b-1 or now_c == b+1 or now_c == 2*b:
				flag = 0
				break

			if 0 <= b - 1 <= 200000 and visited[b - 1] == 0:
				que.append([now_c, b - 1, t])
				visited[b - 1] == 1
			if 0 <= b + 1 <= 200000 and visited[b + 1] == 0:
				que.append([now_c, b + 1, t])
				visited[b + 1] == 1
			if 0 <= 2 * b <= 200000 and visited[2 * b] == 0:
				que.append([now_c, 2 * b, t])
				visited[2 * b] == 1

	return t

# print(catch_me(c, b))  # 5가 나와야 합니다!
# print("정답 = 3 / 현재 풀이 값 = ", catch_me(10, 3))
# print("정답 = 8 / 현재 풀이 값 = ", catch_me(51, 50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550, 500))
