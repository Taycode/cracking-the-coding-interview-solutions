"""
Given two strings, write a method to decide if one is a permutation of the
other
"""


def is_permutation(first_string, second_string):
	"""

	:param first_string: string
	:param second_string: string
	:return: boolean
	"""

	the_dict = {}

	for _ in first_string:
		if _ not in the_dict.keys():
			the_dict[_] = 1
		else:
			the_dict[_] += 1

	for _ in second_string:
		if _ not in the_dict.keys():
			return False
		else:
			the_dict[_] -= 1

	if max(list(the_dict.values())) > 0:
		return False

	else:
		return True


print(is_permutation('dogs', 'gosd'))
