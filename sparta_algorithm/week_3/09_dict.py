class Dict:
	def __init__(self):
		self.items = [None] * 8

	def put(self, key, value):
		index = hash(key) % len(self.items)
		# 같은 index가 배정될 수 있음
		# 링크드 리스트를 써서 노드로 이어주기
		# 이때, 키를 함께 써서 어떤 value가 나와야하는지 명시
		self.items[index] = value

	def get(self, key):
		index = hash(key) % len(self.items)
		return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))