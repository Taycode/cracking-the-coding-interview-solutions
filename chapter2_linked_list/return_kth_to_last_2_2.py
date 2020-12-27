""""
Implement an algorithm to find the kth to last element of a singly linked list.
"""


class Node(object):
	"""Linked List Node"""

	def __init__(self, value=None):
		self.value = value
		self.next = None
		self.previous = None

	def add_next(self, node):
		"""
		Adds Next Node

		:param node: Node
		:return: Node
		"""

		self.next = node
		self.next.previous = self
		return self

	def convert_to_list(self):
		"""

		:return: list
		"""

		the_list = []

		node = self

		while node:
			the_list.append(node.value)
			node = node.next
		return the_list


def get_sliced_linked_list(head_node, k):
	"""

	:param head_node: Node
	:param k: int
	:return: list
	"""

	node = head_node
	count = 0

	while node:
		count += 1
		node = node.next

		if k == count:
			break

	print(node.convert_to_list())


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(3)
f = Node(2)

a.add_next(b)
b.add_next(c)
c.add_next(d)
d.add_next(e)
e.add_next(f)

get_sliced_linked_list(a, 3)
