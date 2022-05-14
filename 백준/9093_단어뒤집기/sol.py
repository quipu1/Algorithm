import sys
sys.stdin = open("input.txt")

T = int(sys.stdin.readline())

for i in range(0, T):
	result = ""
	words = sys.stdin.readline().split()
	for word in words:
		result += word[::-1]
		result += " "
	print(result)

