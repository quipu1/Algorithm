k = 4  # 말의 개수

chess_map = [
    [0, 0, 2, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 2],
    [0, 2, 0, 0]
]
start_horse_location_and_directions = [
    [1, 0, 0],
    [2, 1, 2],
    [1, 1, 0],
    [3, 0, 1]
]
# k = 4  # 말의 개수
#
# chess_map = [
# 	[0, 0, 0, 0],
# 	[0, 0, 0, 0],
# 	[0, 0, 0, 0],
# 	[0, 0, 0, 0]
# ]
# start_horse_location_and_directions = [
# 	[0, 0, 0],
# 	[0, 1, 0],
# 	[0, 2, 0],
# 	[2, 2, 2]
# ]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def blue(direction, location_x, location_y):
	if direction == 0:
		direction = 1
	elif direction == 1:
		direction = 0
	elif direction == 2:
		direction = 3
	elif direction == 3:
		direction = 2

	for d in range(4):
		if direction == d:
			next_x = location_x + dr[d]
			next_y = location_y + dy[d]

	return next_x, next_y, direction


def check(visit_map, x, y):
	if len(visit_map[x][y]) >= 4:
		return True
	return False


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
	turn = 0
	stop = 0
	N = len(game_map)
	visit = [[""] * N for i in range(N)]

	for i in range(len(horse_location_and_directions)):
		visit[horse_location_and_directions[i][0]][horse_location_and_directions[i][1]] += str(i)

	while turn < 1000:

		turn += 1

		for i in range(len(horse_location_and_directions)):
			location_x, location_y, direction = horse_location_and_directions[i][0], horse_location_and_directions[i][1], horse_location_and_directions[i][2]
			# 다음에 갈 위치
			for d in range(4):
				if direction == d:
					next_x = location_x + dr[d]
					next_y = location_y + dy[d]
					break

			# 현재 쌓아진 말 확인
			top = ""
			visited = visit[location_x][location_y]
			index = visited.find(str(i))
			top += visited[index:]

			# 다음 칸이 파란색이거나 범위를 벗어날 경우
			if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N or game_map[next_x][next_y] == 2:
				blue_x, blue_y, blue_d = blue(direction, location_x, location_y)
				horse_location_and_directions[i][2] = blue_d
				if game_map[blue_x][blue_y] == 2 or blue_x < 0 or blue_x >= N or blue_y < 0 or blue_y >= N:
					pass
				else:
					# 방문했던 기록 지우기
					visit[location_x][location_y] = visited[0:index]
					# 쌓아진 거 이동
					for t in top:
						horse_location_and_directions[int(t)][0], horse_location_and_directions[int(t)][1] = blue_x, blue_y
						visit[blue_x][blue_y] += t
					if check(visit, blue_x, blue_y):
						return turn

			# 다음 칸이 흰색일 경우
			elif game_map[next_x][next_y] == 0:
				# 방문했던 기록 지우기
				visit[location_x][location_y] = visited[0:index]
				# 쌓아진 거 이동
				for t in top:
					horse_location_and_directions[int(t)][0], horse_location_and_directions[int(t)][1] = next_x, next_y
					visit[next_x][next_y] += t
				if check(visit, next_x, next_y):
					return turn
			# 다음 칸이 빨간색일 경우
			elif game_map[next_x][next_y] == 1:
				# 방문했던 기록 지우기
				visit[location_x][location_y] = visited[0:index]
				# 쌓아진 거 이동
				top = top[::-1]
				for t in top:
					horse_location_and_directions[int(t)][0], horse_location_and_directions[int(t)][1] = next_x, next_y
					visit[next_x][next_y] += t
				if check(visit, next_x, next_y):
					return turn

		if stop:
			return turn

	return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

# start_horse_location_and_directions = [
# 	[0, 1, 0],
# 	[1, 1, 0],
# 	[0, 2, 0],
# 	[2, 2, 2]
# ]
# print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))
#
# start_horse_location_and_directions = [
# 	[0, 1, 0],
# 	[0, 1, 1],
# 	[0, 1, 0],
# 	[2, 1, 2]
# ]
# print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))