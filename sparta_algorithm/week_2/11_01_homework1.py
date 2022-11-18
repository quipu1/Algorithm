class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self, data):
		self.head = Node(data)

	def append(self, data):
		cur = self.head
		while cur.next is not None:
			cur = cur.next
		cur.next = Node(data)

	def get_kth_node_from_last(self, k):
		cur = self.head
		node_length = 0
		while cur.next is not None:
			cur = cur.next
			node_length += 1

		now_length = 0
		now = self.head
		while now_length != node_length - k + 1:
			now = now.next
			now_length += 1

		return now


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)