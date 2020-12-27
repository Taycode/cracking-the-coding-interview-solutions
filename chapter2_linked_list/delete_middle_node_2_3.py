"""
Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e- >f
"""


class Node(object):
	"""Linked List Node"""

	def __init__(self, value=None):
		self.value = value
		self.next = None

	def add_next(self, node):
		"""
		Adds Next Node

		:param node: Node
		:return: Node
		"""

		self.next = node
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


def delete_node(linked_list, node):
	"""

	:param linked_list: Node
	:param node: Node
	:return: Node
	"""

	head_node = linked_list
	previous = None
	while head_node:
		if node.value == head_node.value:
			previous.next = head_node.next
			break
		else:
			previous = head_node
		head_node = head_node.next


print(a.convert_to_list())

delete_node(a, b)

print(a.convert_to_list())
