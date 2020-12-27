"""
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
->
pales, pale -> true
pale, bale -> true
pale, bake -> true
pale, ple -> false
"""


def one_way(first_string, second_string):
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
			the_dict[_] = -1
		else:
			the_dict[_] -= 1

		if the_dict[_] == 0:
			the_dict.pop(_)

	values = list(the_dict.values())

	if len(values) > 2:
		return False

	if len(values) == 2 and min(*values) and sum(values) == 0:
		return True

	if not values:
		return True

	if -1 <= values[0] <= 1:
		return True

	return False


print(one_way('bale', 'bake'))
