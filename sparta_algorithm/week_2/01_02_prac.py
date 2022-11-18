class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self, data):
		self.head = Node(data)

	def append(self, data):
		if self.head is None:
			self.head = Node(data)
			return

		cur = self.head
		# 다음 값이 없을 때까지 넘기기
		# 리스트의 맨 끝 값으로 가서 그 값의 next 값을 넣는다
		while cur.next is not None:
			cur = cur.next
		cur.next = Node(data)

	def print_all(self, data):
			cur = self.head
			while cur is not None:
				print(cur.data)
				cur = cur.next



