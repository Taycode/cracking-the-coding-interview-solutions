"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def compressor(string):
	"""

	:param string: string
	:return: string
	"""

	if not string:
		return ''

	solution = []
	focus = string[0]
	count = 0
	for _ in string:
		if _ != focus:
			solution.append(f'{focus}{count}')
			count = 0
			focus = _
		count += 1
	solution.append(f'{focus}{count}')
	return ''.join(solution)


print(compressor('aaaahhhhhssss'))
