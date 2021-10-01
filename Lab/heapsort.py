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


# Replace this line with code.

def max_heapify(elements, index, len_of_elements):
	"""
	# todo
	Args:
		elements:
		index:

	Returns:

	"""
	largest_ele_index = index
	left = 1 if index == 0 else index * 2
	right = left + 1
	ele = elements [index]
	if left <= len_of_elements and ele < elements [left]:
		largest_ele_index = left
	if right <= len_of_elements and ele < elements [right]:
		largest_ele_index = right
	if largest_ele_index != index:
		# todo - can check if `largest_ele_index`'s left and right are below `len_of_elements`
		elements [index], elements [largest_ele_index] = elements [largest_ele_index], elements [index]
		print("Swap:\n")
		print(elements)
		max_heapify(elements, largest_ele_index, len_of_elements)


def build_max_heap(elements):
	"""

	Args:
		elements:

	Returns:

	"""
	length_of_elements = len(elements) - 1
	middle_ele = (length_of_elements) // 2
	print(length_of_elements, middle_ele)
	while middle_ele >= 0:
		max_heapify(elements, middle_ele, length_of_elements)
		middle_ele = middle_ele - 1


if __name__ == '__main__':
	normal_list = [10, 20, 25, 6, 12, 15, 4, 16]
	print(normal_list)
	max_heapify(normal_list, 0, len(normal_list) - 1)
	print(normal_list)

	build_max_heap(normal_list)
	print(normal_list)
