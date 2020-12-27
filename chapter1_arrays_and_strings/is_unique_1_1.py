"""
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""


def is_unique(string):
	"""

	:param string: string
	:return: Boolean
	"""
	the_dict = {}
	for _ in string:
		if _ in the_dict.keys():
			return False
		the_dict[_] = True

	return True


print(is_unique('asfsire'))
