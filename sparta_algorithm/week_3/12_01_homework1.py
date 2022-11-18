shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
	prices = sorted(prices)
	coupons = sorted(coupons)
	sum_price = 0

	for i in range(len(prices)):
		if len(coupons) == 0:
			sum_price += sum(prices)
			break
		coupon = coupons.pop()
		price = prices.pop()
		sum_price += price * (100 - coupon) / 100

	return int(sum_price)


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))