"""
# Docstring.
"""


# Python Modules
# -N/A

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A


def insertion_sort(array_ele):
	"""

	Args:
		array_ele:

	Returns:

	"""
	if len(array_ele) == 1:
		return
	for j in range(1, len(array_ele)):
		if array_ele [j] < array_ele [j - 1]:
			# print("--------------------------------")
			print(array_ele [:j + 1])
			for i in range(j, 0, -1):
				if array_ele [i] < array_ele [i - 1]:
					# print("Swapping............")
					array_ele [i], array_ele [i - 1] = array_ele [i - 1], array_ele [i]
				else:
					break
				print(array_ele [:j + 1])


if __name__ == '__main__':
	normal_list = [10, 20, 25, 6, 12, 15, 4, 16, 4, -1, 32432]
	# normal_list = [-1, 0, 1, 2, -1, 0, 10]
	print("The unsorted list is : {}".format(normal_list))
	insertion_sort(normal_list)
	print("The sorted list is : {}".format(normal_list))
