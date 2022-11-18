from collections import deque

game_map = [
	["#", "#", "#", "#", "#"],
	["#", ".", ".", "B", "#"],
	["#", ".", "#", ".", "#"],
	["#", "R", "O", ".", "#"],
	["#", "#", "#", "#", "#"],
]

N = len(game_map)
M = len(game_map[0])


def blue_check(map, b_location, direction_x, direction_y):

	while 0 <= b_location[0] < N and 0 <= b_location[1] < M:
		if map[b_location[0]][b_location[1]] == 'O':
			return False
		elif game_map[b_location[0]][b_location[1]] == '#':
			return b_location
		b_location[0] = b_location[0] + direction_x
		b_location[1] = b_location[1] + direction_y


def is_available_to_take_out_only_red_marble(game_map):
	red = []
	blue = []

	for i in range(N):
		if red and blue:
			break
		for j in range(M):
			if game_map[i][j] == 'R':
				red = [i, j]
			if game_map[i][j] == 'B':
				blue = [i, j]

	que = deque([])
	que.append([red, blue, 0])

	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]

	while True:
		now = que.popleft()
		now_red, now_blue, now_turn = now[0], now[1], 0
		now_turn += 1

		if now_turn > 10:
			return -1

		for i in range(4):
			red_hole = 0
			red_x = now_red[0] + dx[i]
			red_y = now_red[1] + dy[i]

			while 0 <= red_x < N and 0 <= red_y < M:
				if game_map[red_x][red_y] == 'O':
					red_hole = 1
					break
				elif game_map[red_x][red_y] == '#':
					break

				red_x = red_x + dx[i]
				red_y = red_y + dy[i]

			b = blue_check(game_map, now_blue, dx[i], dy[i])

			# 파란색 상태 확인
			if b and red_hole == 1:
				return True
			elif b is False:
				pass
			else:
				que.appendleft([[red_x, red_y], b, now_turn])




print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
	["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
	["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
	["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
	["#", "#", "#", "#", "#", "#", "#"],
	["#", ".", ".", "R", "#", "B", "#"],
	["#", ".", "#", "#", "#", "#", "#"],
	["#", ".", ".", ".", ".", ".", "#"],
	["#", "#", "#", "#", "#", ".", "#"],
	["#", "O", ".", ".", ".", ".", "#"],
	["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))