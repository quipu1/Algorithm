seat_count = 9
vip_seat_array = [4, 7]

memo = {
	1: 1,
	2: 2,
}


def fibo(n, fibo_memo):
	if n <= 2:
		return fibo_memo[n]

	nth_fibo = fibo(n-1, fibo_memo) + fibo(n-2, fibo_memo)
	fibo_memo[n] = nth_fibo
	return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
	cnt = 1
	now_seat = 1

	for fix in fixed_seat_array:
		cnt *= fibo(fix - now_seat, memo)
		now_seat = fix + 1

	cnt *= fibo(total_count - now_seat + 1, memo)

	return cnt


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))