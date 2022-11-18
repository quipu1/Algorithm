input = 20


def find_prime_list_under_number(number):
	prime = []
	for n in range(number):
		if n <= 1:
			pass
		elif n == 2:
			prime.append(n)
		else:
			not_prime = 0
			for i in range(2, n):
				# 나머지가 있으면
				if n%i:
					pass
				else:
					not_prime = 1
					break
			if not_prime == 0:
				prime.append(n)

	return prime


result = find_prime_list_under_number(input)
print(result)

# 해설
def find_prime_list_under_number(number):
	prime_list = []
	for n in range(2, number+1):
		for i in range(2, n):
			if n % i == 0:
				break
		else:
			prime_list.append(n)

	return prime_list