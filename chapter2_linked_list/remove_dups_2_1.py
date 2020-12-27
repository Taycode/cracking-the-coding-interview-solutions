"""
Write code to remove duplicates from an unsorted linked list.
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


def remove_duplicates(head_node):
	"""

	:param head_node: node
	:return: node
	"""

	node = head_node
	the_dict = {}

	while node:

		if node.value in the_dict.keys():
			node.previous.next = node.next
			if node.next:
				node.next.previous = node.previous
		else:
			the_dict[node.value] = True
		node = node.next


print(a.convert_to_list())

remove_duplicates(a)

print(a.convert_to_list())
