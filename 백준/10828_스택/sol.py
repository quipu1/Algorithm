import sys
sys.stdin = open("input.txt")

# 시간초과 문제는 readline()으로 해결
# 하지만, readline의 경우 개행문자도 입력으로 받을 수 있으니 주의
#readline().strip()를 통해 개행문자를 없앨 수 있다!
N = int(sys.stdin.readline())

stack = []

for i in range(0,N):
	a = sys.stdin.readline().split()
	if a[0] == 'push':
		stack.append(a[1])
	elif a[0] == 'pop':
		if len(stack) == 0:
			print(-1)
		else:
			print(stack.pop())
	elif a[0] == 'size':
		print(len(stack))
	elif a[0] == 'empty':
		if len(stack) == 0:
			print(1)
		else:
			print(0)
	elif a[0] == 'top':
		if len(stack) == 0:
			print(-1)
		else:
			print(stack[-1])