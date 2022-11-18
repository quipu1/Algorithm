from collections import deque

game_map = [
	["#", "#", "#", "#", "#"],
	["#", ".", ".", "B", "#"],
	["#", ".", "#", ".", "#"],
	["#", "R", "O", ".", "#"],
	["#", "#", "#", "#", "#"],
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move_ball(game_map, d_x, d_y, x, y):
	go = 0
	while game_map[x+d_x][y+d_y] != '#' and game_map[x][y] != 'O':
		x += d_x
		y += d_y
		go += 1
	return x, y, go

def is_available_to_take_out_only_red_marble(game_map):
	n = len(game_map)
	m = len(game_map[0])
	turn = 0
	red_x, red_y, blue_x, blue_y = 0, 0, 0, 0

	# red, blue 위치
	for i in range(n):
		for j in range(m):
			if game_map[i][j] == 'R':
				red_x = i
				red_y = j
			elif game_map[i][j] == 'B':
				blue_x = i
				blue_y = j

	r_visited = [[False] * m for _ in range(n)]
	b_visited = [[False] * m for _ in range(n)]
	r_visited[red_x][red_y] = True
	b_visited[blue_x][blue_y] = True

	que = deque([])
	que.append((red_x, red_y, blue_x, blue_y, turn))

	while que:
		r_x, r_y, b_x, b_y, now_t = que.popleft()

		if now_t > 10:
			break

		for d in range(4):
			next_r_x, next_r_y, r_go = move_ball(game_map, dx[d], dy[d], r_x, r_y)
			next_b_x, next_b_y, b_go = move_ball(game_map, dx[d], dy[d], b_x, b_y)

			if game_map[next_b_x][next_b_y] == 'O':
				continue
			if game_map[next_r_x][next_r_y] == 'O':
				return True
			if next_r_x == next_b_x and next_r_y == next_b_y:
				if r_go > b_go:
					next_r_x -= dx[d]
					next_r_y -= dy[d]
				else:
					next_b_x -= dx[d]
					next_b_y -= dy[d]
			if r_visited[next_r_x][next_r_y] is False and b_visited[next_b_x][next_b_y] is False:
				r_visited[next_r_x][next_r_y] = True
				b_visited[next_b_x][next_b_y] = True
				que.append((next_r_x, next_r_y, next_b_x, next_b_y, now_t + 1))

	return False






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