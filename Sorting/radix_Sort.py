"""
# Docstring.
"""
# Python Modules

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
get_digit = lambda number, base: (number // base) % 10


def get_count_of_ele(elements, base):
	"""

	Args:
		elements:
		base:

	Returns:

	"""
	count_of_ele = [0 for _ in range(10)]
	for ele in elements:
		try:
			count_of_ele [get_digit(ele, base)] += 1
		except Exception as e:
			print(ele, e)
	for index in range(1, 10):
		count_of_ele [index] += count_of_ele [index - 1]

	return count_of_ele


def counting_sort(elements, count_array, base):
	"""

	Args:
		elements:
		count_array:
		base:

	Returns:

	"""
	# init storage array
	sorted_array = [0 for i in range(count_array [-1])]
	for i in range(len(elements) - 1, -1, -1):
		ele = elements [i]
		digit_index = get_digit(ele, base)
		count_array [digit_index] -= 1
		count = count_array [digit_index]
		# Storing the actual element
		sorted_array [count] = ele

	print(sorted_array)
	for index, ele in enumerate(sorted_array):
		elements [index] = ele


def radix_sort(elements):
	"""

	Args:
		elements:

	Returns:

	"""
	base = 1
	max_element = max(elements)
	while max_element // base > 0:
		count_array = get_count_of_ele(elements, base)
		counting_sort(elements, count_array, base)
		base *= 10


if __name__ == '__main__':
	arr = [573, 25, 415, 12, 161, 6]
	print(arr)
	radix_sort(arr)
	print(arr)
