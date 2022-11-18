import itertools, sys

n = 5
m = 3

city_map = [
	[0, 0, 1, 0, 0],
	[0, 0, 2, 0, 1],
	[0, 1, 2, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 0, 2],
]


def get_house_chicken_distance(chicken, houses):
	chicken_house_distances = []
	for house in houses:
		chicken_house_distances.append(abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))

	return chicken_house_distances


def get_chicken_house_distance(chickens, house):
	house_chicken_distances = []
	for chicken in chickens:
		house_chicken_distances.append(abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))

	return min(house_chicken_distances)


def get_min_city_chicken_distance(n, m, city_map):
	chickens = []
	houses = []
	for i in range(n):
		for j in range(n):
			if city_map[i][j] == 1:
				houses.append([i, j])
			elif city_map[i][j] == 2:
				chickens.append([i, j])

	chicken_distances = []
	for chicken in chickens:
		chicken_distances.append(get_house_chicken_distance(chicken, houses))

	sum_chicken_distances = {}
	for i in range(len(chicken_distances)):
		sum_chicken_distances[i] = sum(chicken_distances[i])

	sort_sum_chicken_distances = sorted(sum_chicken_distances.items(), key=lambda distances: distances[1])

	#  m개의 치킨집들의 인덱스
	m_chickens = []
	for i in range(m):
		m_chickens.append(chickens[sort_sum_chicken_distances[i][0]])


	#각 집의 치킨 최소거리!
	min_distance = 0
	for house in houses:
		min_distance += get_chicken_house_distance(m_chickens, house)

	return min_distance

# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!


city_map = [
	[1, 2, 0, 0, 0],
	[1, 2, 0, 0, 0],
	[1, 2, 0, 0, 0],
	[1, 2, 0, 0, 0],
	[1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))


city_map = [
	[0, 2, 0, 1, 0],
	[1, 0, 1, 0, 0],
	[0, 0, 0, 0, 0],
	[2, 0, 0, 1, 1],
	[2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))