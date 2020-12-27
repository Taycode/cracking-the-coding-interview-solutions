"""
Implement a function to check if a linked list is a palindrome.
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
b = Node(1)
c = Node(1)
d = Node(1)
e = Node(1)
f = Node(1)

a.add_next(b)
b.add_next(c)
c.add_next(d)
d.add_next(e)
e.add_next(f)


class Solution:
	"""Solution Class"""

	@staticmethod
	def check_palindrome(head):
		"""

		:param head:
		:return:
		"""
