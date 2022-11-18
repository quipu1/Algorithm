from collections import deque

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

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def left_direction(d):
	new_d = (d + 3) % 4
	return new_d


def back_index(d):
	new_d = (d + 2) % 4
	return new_d


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
	n = len(room_map)
	m = len(room_map[0])

	cnt = 1
	room_map[r][c] = 2

	que = deque([[r, c, d]])

	while que:
		r, c, d = que.popleft()
		temp_d = d

		for i in range(4):
			now_d = left_direction(temp_d)
			next_r = r + dr[i]
			next_c = c + dc[i]

			if 0 <= next_r < n and 0 <= next_c < m and room_map[next_r][next_c] == 0:
				room_map[next_r][next_c] == 2
				cnt += 1
				que.append([next_r, next_c, now_d])
				break

			elif i == 3:
				new_r, new_c = r + dr[back_index(r)], c + dc[back_index(c)]
				que.append([new_r, new_c, d])

				if room_map[new_r][new_c] == 1:
					return cnt



# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
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
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6, 3, 1, current_room_map2))
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
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7, 4, 1, current_room_map3))
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
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6, 2, 0, current_room_map4))
