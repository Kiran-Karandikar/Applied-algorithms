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


def max_heapify(elements, index, len_of_elements):
	"""
	# todo
	Args:
	 len_of_elements:
		elements:
		index:

	Returns:

	"""
	largest_ele_index = None
	largest_element = elements [index]
	is_max_element = False
	left = (2 * index) + 1
	right = left + 1
	if left < len_of_elements and largest_element < elements [left]:
		largest_ele_index = left
		largest_element = elements [left]
		is_max_element = True
	if right < len_of_elements and largest_element < elements [right]:
		largest_ele_index = right
		largest_element = elements [right]
		is_max_element = True
	if is_max_element:
		# todo - can check if `largest_ele_index`'s left and right are below `len_of_elements`
		elements [index], elements [largest_ele_index] = largest_element, elements [index]
		max_heapify(elements, largest_ele_index, len_of_elements)


def build_max_heap(all_elements):
	"""

	Args:
		all_elements:

	Returns:

	"""
	total_elements = len(all_elements)
	middle_element_index = total_elements // 2
	if total_elements % 2 == 0:
		middle_element_index = middle_element_index - 1
	for index in range(middle_element_index, -1, -1):
		max_heapify(all_elements, index, total_elements)


def heap_sort(array_ele, is_heapified = False):
	"""

	Args:
	 is_heapified:
		array_ele:

	Returns:

	"""
	if not is_heapified:
		build_max_heap(array_ele)
		print("Built max heap .....")
	for _ in range(len(array_ele), 1, -1):
		yield array_ele.pop(0)
		array_ele.insert(0, array_ele.pop(-1))
		build_max_heap(array_ele)
	yield array_ele.pop(0)


if __name__ == '__main__':
	normal_list = [10, 20, 25, 6, 12, 15, 4, 16]
	normal_list = [-1, 0, 1, 2, -1, 0, 10]
	print("The unsorted list is : {}".format(normal_list))
	build_max_heap(normal_list)
	print("Build Max heap: {}".format(normal_list))
	for i in heap_sort(normal_list, is_heapified=True):
		print(i)
