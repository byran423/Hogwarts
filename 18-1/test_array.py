class Array:
	def __init__(self, capacity) -> None:
		self.data = [-1] * capacity
		self.count = 0
		self.n = capacity

	def insert(self, location, value):
		if self.n == self.count:
			return False
		if location < 0 or location > self.count:
			return False
		for i in range(self.count, location, -1):
			self.data[i] = self.data[i - 1]

		self.data[location] = value
		self.count += 1
		return True

	def find(self, location):
		if location < 0 or location > self.count:
			return -1
		return self.data[location]

	def delete(self, location):
		if location < 0 or location > self.count:
			return False
		for i in range(location + 1, self.count):
			self.data[i - 1] = self.data[i]
		self.count -= 1
		return True


def test_demo():
	array = Array(5)
	array.insert(0, 1)
	array.insert(0, 2)
	array.insert(1, 3)
	array.insert(2, 4)
	array.insert(4, 5)
	print(array.data)
