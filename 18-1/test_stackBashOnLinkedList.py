class StackBaskOnLinkedList:
	def __init__(self) -> None:
		self.top = None

	def push(self, value):
		new_node = self.Node(value)
		if self.top is None:
			self.top = new_node
		else:
			new_node.next = self.top
			self.top = new_node

	def pop(self):
		if self.top is None:
			return -1
		result = self.top.data
		self.top = self.top.next
		return result

	class Node:
		def __init__(self, data) -> None:
			self.data = data
			self.next = None
