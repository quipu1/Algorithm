import sys
sys.stdin = open("input.txt")

T = int(sys.stdin.readline())

for i in range(0,T):
	data = sys.stdin.readline()
	sum = 0
	for d in data:
		if d == '(':
			sum += 1
		elif d == ')':
			sum -= 1
			if sum < 0:
				break
	if sum == 0:
		print("YES")
	else:
		print("NO")