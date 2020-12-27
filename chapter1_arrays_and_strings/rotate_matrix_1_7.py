"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

array = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]


def array_rotator(array_2d):
	"""

	:param array_2d: 2d array
	:return: 2d array
	"""

	solution = []
	length = len(array_2d)
	column = 0
	while column < length:
		row = length - 1
		column_data = []
		while row >= 0:
			focus_row = array_2d[row]
			value = focus_row[column]
			column_data.append(value)
			row -= 1

		solution.append(column_data)
		column += 1

	return solution


print(array_rotator(array))



