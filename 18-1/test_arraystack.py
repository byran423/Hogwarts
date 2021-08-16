class ArrayStack:
	def __init__(self, n) -> None:
		self.data = [-1] * n
		self.n = n
		self.count = 0

	def push(self, value):
		if self.n == self.count:
			return False
		self.data[self.count] = value
		self.count += 1
		return True

	def pop(self):
		if self.count == 0:
			return None

		self.count -= 1
		return self.data[self.count]

