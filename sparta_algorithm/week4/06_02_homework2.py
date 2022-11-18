current_r, current_c, current_d = 7, 4, 0
current_room_map = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
	[1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

visited = []
count = 0

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map, visit, cnt):
	# 현재 위치 r,c 보는 방향 d
	# r은 아래로 얼마나 c는 오른쪽으로 얼마나 떨어져있는지 청소기 위치
	# d = 0 상 / 1 우 / 2 하 / 3 좌
	# map 0은 빈칸, 1은 벽
	# 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색
	# 현재 위치에서 왼쪽에 청소할 게 있다면 왼쪽으로,
	# 왼쪽에 없다면 바라보는 방향

	now = [r, c]

	# 현재 위치 청소
	cnt += 1
	visit.append(now)

	# 왼쪽 방향부터 차례대로 탐색 진행
	if d == 0:
		now_next = [r, c-1]
		if now_next is not visit and room_map[now_next[0]][now_next[1]] == 0:
			now = now_next
			get_count_of_departments_cleaned_by_robot_vacuum(now[0], now[1], 3, room_map, visit, cnt)
	elif d == 1:
		now_next = [r-1, c]
		if now_next is not visit and room_map[now_next[0]][now_next[1]] == 0:
			now = now_next
			get_count_of_departments_cleaned_by_robot_vacuum(now[0], now[1], 0, room_map, visit, cnt)
	elif d == 2:
		now_next = [r, c+1]
		if now_next is not visit and room_map[now_next[0]][now_next[1]] == 0:
			now = now_next
			get_count_of_departments_cleaned_by_robot_vacuum(now[0], now[1], 1, room_map, visit, cnt)
	else:
		now_next = [r+1, c]
		if now_next is not visit and room_map[now_next[0]][now_next[1]] == 0:
			now = now_next
			get_count_of_departments_cleaned_by_robot_vacuum(now[0], now[1], 4, room_map, visit, cnt)

	# 네방향 모두 청소가 이미 되어있거나 벽인 경우
	if ([r, c-1] in visit or room_map[r][c-1] == 1) and ([r, c+1] in visit or room_map[r][c+1] == 1) and ([r-1, c] in visit or room_map[r-1][c] == 1) and ([r+1, c+1] in visit or room_map[r][c-1] == 1):
		# 네방향 모두 청소가 이미 되어있거나 벽인 경우 + 후진 불가
		if (d == 0 and room_map[r+1][c] == 1) or (d == 1 and room_map[r][c-1] == 1) or (d == 2 and room_map[r-1][c] == 1) or (d == 3 and room_map[r][c+1] == 1):
			return cnt
		else:
			if d == 0:
				get_count_of_departments_cleaned_by_robot_vacuum(now[0]+1, now[1], d, room_map, visit, cnt)
			elif d == 1:
				get_count_of_departments_cleaned_by_robot_vacuum(now[0], now[1]-1, d, room_map, visit, cnt)
			elif d == 1:
				get_count_of_departments_cleaned_by_robot_vacuum(now[0]-1, now[1], d, room_map, visit, cnt)
			else:
				get_count_of_departments_cleaned_by_robot_vacuum(now[0], now[1]+1, d, room_map, visit, cnt)

	return cnt


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map, visited, count))
current_room_map2 = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
	[1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2, visited, count))
current_room_map3 = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
	[1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
	[1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3, visited, count))
current_room_map4 = [
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
	[1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
	[1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,2,0,current_room_map4, visited, count))