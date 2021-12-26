"""
# Docstring.
"""

# Python Modules
from random import choice


# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A


def divide_array(array_ele, left, right):
	"""

	Args:
		array_ele:
		left:
		right:

	Returns:

	"""
	pivot_index = choice(range(left, right))
	pivot_ele = array_ele [pivot_index]

	# fix: what about duplicates ????
	bigger_element_index = -1
	for index in range(0, len(array_ele)):
		if array_ele [index] > pivot_ele and bigger_element_index == -1:
			bigger_element_index = index
		if array_ele [index] < pivot_ele and bigger_element_index != -1:
			array_ele [index], array_ele [bigger_element_index] = array_ele [bigger_element_index], array_ele [index]
			bigger_element_index += 1

	large_ele = array_ele [bigger_element_index]
	if bigger_element_index != -1
		if bigger_element_index > pivot_index and large_ele < pivot_ele:

		if bigger_element_index < pivot_index:
			array_ele [bigger_element_index]
		pivot_ele:
		array_ele [pivot_index], array_ele [bigger_element_index] = array_ele [bigger_element_index], array_ele [
			pivot_index]
	else:
		bigger_element_index = pivot_index

	return bigger_element_index


def quick_sort(array_ele, left, right):
	"""

	Args:
		array_ele:
		left:
		right:

	Returns:

	"""

	if left < right:
		pivot_index = divide_array(array_ele, left, right)
		quick_sort(array_ele, left, pivot_index)
		quick_sort(array_ele, pivot_index + 1, right)


if __name__ == '__main__':
	normal_list = [10, 20, 25, 6, 12, 15, 4, 16, 4, -1, 32432]
	# normal_list = [-1, 0, 1, 2, -1, 0, 10]
	print("The unsorted list is : {}".format(normal_list))
	quick_sort(normal_list, 0, len(normal_list) - 1)
