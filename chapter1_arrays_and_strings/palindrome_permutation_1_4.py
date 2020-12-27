"""
Given a string, write a function to check if it is a permutation of a palin­
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""


def palindrome_permutation(string):
	"""

	:param string: string
	:return: boolean
	"""

	the_dict = {}
	string = string.replace(' ', '')
	string = string.lower()
	for _ in string:
		if _ not in the_dict.keys():
			the_dict[_] = 1

		else:
			the_dict[_] += 1

	values = list(the_dict.values())

	length = len(string)

	if length % 2 == 0:
		for _ in values:
			if _ % 2 != 0:
				return False
		else:
			return True
	else:
		count = 0 
		for _ in values:
			if _ % 2 != 0:
				count += 1
				if count > 1:
					return False
		else:
			return True


print(palindrome_permutation('Tact Coa'))
