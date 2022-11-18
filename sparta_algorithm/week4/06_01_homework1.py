import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
	# 하루에 1톤씩
	# 최소한의 횟수로 밀가루 공급 => 운송비 때문
	# 현재 공장에 남아있는 밀가루 수량 stock
	# 원래 공장으로부터 공급받을 수 있는 시점 k
	# 밀가루가 안 떨어지게 해외에서 최소한 몇 번 공급받아야하는지

	cnt = 0
	sum_supply = 0
	need_stock = k - stock
	supply = {}
	for s in range(len(dates)):
		supply[dates[s]] = supplies[s]

	sort_supply = sorted(supply.items(), key=lambda item: item[1], reverse=True)

	for i in range(len(sort_supply)):
		sum_supply += sort_supply[i][1]
		cnt += 1
		if sum_supply >= need_stock:
			break

	return cnt


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))