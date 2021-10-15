"""
# Docstring.
"""
# Python Modules
from random import sample, seed
from timeit import Timer

from matplotlib import pyplot as plt


# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A


def get_count_of_ele(elements, max_element):
	"""

	Args:
		elements:
		max_element: range of elements, maximum element in `list of ele`

	Returns:

	"""
	total_elements = len(elements)
	# fix: for python list, index starts at zero
	k = max(total_elements, max_element) + 1
	count_of_ele = [0 for _ in range(k)]
	# print(elements, count_of_ele, max_element, total_elements)
	# Populate the count array with maximum number of elements.
	for ele in elements:
		try:
			count_of_ele [ele] += 1
		except Exception as e:
			print(ele, e)
	# print(count_of_ele)
	for index in range(1, k):
		count_of_ele [index] += count_of_ele [index - 1]

	return count_of_ele


def counting_sort(elements, count_array = None):
	"""

	Args:
		elements:
		count_array:

	Returns:

	"""
	if count_array is None:
		count_array = get_count_of_ele(elements, max(elements))
	# init storage array
	sorted_array = [0 for i in range(count_array [-1])]
	# print(sorted_array, len(sorted_array), count_array [-1])
	# for index, ele in enumerate(sorted_array):
	# 	print(index, ele)
	for index, ele in enumerate(elements):
		count = count_array [ele]
		# Storing the actual element
		# fix: for python list instead of putting at the exact `count`, since list start with 0 index
		sorted_array [count - 1] = ele
		# print("-----------------------------")
		# print(elements)
		# print(count_of_ele)
		# print([_ for _ in range(8)])
		# print(sorted_array)
		count_array [ele] = count - 1
	return sorted_array


if __name__ == '__main__':
	# list_of_ele = [2, 5, 3, 0, 2, 3, 0, 3]
	# list_of_ele = [5, 1, 3, 0, 4, 2, 6, 3, 1, 2]
	# list_of_ele = [99, 1, 3, 0, 4, 2, 89, 3, 1, 7855]
	# k = max(list_of_ele)
	# count_of_ele = get_count_of_ele(list_of_ele, k)
	# # pprint(counting_sort(list_of_ele, count_of_ele))
	# pprint(counting_sort(list_of_ele))
	avg_run_time = []
	for i in range(30):
		seed(50)
		s = sample(range(0, 200), i + 1)
		t = Timer(lambda: counting_sort(s))
		run_time = t.timeit()
		avg_run_time.append(run_time)
	with plt.style.context('Solarize_Light2'):
		plt.plot([i + 1 for i in range(30)], avg_run_time)
		plt.title('Running time v/S n')
		plt.xlabel('N', fontsize=14)
		plt.ylabel('Run time', fontsize=14)
	plt.show()
