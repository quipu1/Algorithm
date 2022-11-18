# 1
genres1 = ["classic", "pop", "classic", "classic", "pop"]
plays1 = [500, 600, 150, 800, 2500]
# 정답 = [4, 1, 3, 0]


# 2
genres2 = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays2 = [2000, 500, 600, 150, 800, 2500, 2000]
# 정답 = [0, 6, 5, 2, 4, 1]


def pick_album(genres, plays):
	music_list = []
	result = []
	for i in range(len(genres)):
		music = {"play": plays[i], "genre": genres[i]}
		music_list.append(music)

	# 속한 노래가 많이 재생된 장르
	genre_type = list(set(genres))
	genre_list = {}

	for i in range(len(genre_type)):
		genre_list[genre_type[i]] = 0

	for i in range(len(music_list)):
		genre_list[music_list[i]["genre"]] += music_list[i]["play"]

	most_genre_play = sorted(genre_list.items(), key=lambda x: x[1], reverse=True)

	for i in range(len(music_list)):
		for j in range(len(most_genre_play)):
			if most_genre_play[j][0] == music_list[i]["play"]:
				pass


	return result


print(pick_album(genres1, plays1))
print(pick_album(genres2, plays2))

