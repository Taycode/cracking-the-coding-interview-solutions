"""
You have two numberes represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
Sum Lists: You have two numbers represented by
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
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


class Solution:
	"""Solution Class"""

	@staticmethod
	def get_value(node):
		"""

		:param node: Node
		:return: int
		"""

		if node:
			return node.value

		else:
			return 0

	def sum_lists(self, l1, l2):
		"""

		:param l1: Node
		:param l2: Node
		:return: Node
		"""

		solution_node = Node()
		l1_value = self.get_value(l1)
		l2_value = self.get_value(l2)
		remainder = (l1_value + l2_value) // 10
		solution_node.value = (l1_value + l2_value) % 10

		if l1:
			l1 = l1.next
		if l2:
			l2 = l2.next

		solution_node.next = Node()
		next_node = solution_node.next

		while l1 or l2:

			l1_value = self.get_value(l1)
			l2_value = self.get_value(l2)
			remainder = (l1_value + l1_value + remainder) // 10
			next_node.value = (l1_value + l2_value + remainder) % 10

			next_node.next = Node()
			next_node = next_node.next

			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next

		next_node.value = remainder
		return solution_node


a = Node(1)
b = Node(1)
c = Node(1)
d = Node(1)
e = Node(1)
f = Node(1)

a.add_next(b)
b.add_next(c)
d.add_next(e)
e.add_next(f)

solution = Solution()

print(solution.sum_lists(a, d).convert_to_list())
