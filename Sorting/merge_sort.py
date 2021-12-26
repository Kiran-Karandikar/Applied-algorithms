"""
# Docstring.
"""
# Python Modules
from collections import deque


# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A

def sort_two_dequeue(left_q, right_q):
	"""

	Args:
		left_q:
		right_q:

	Returns:

	"""
	sorted_q = deque()
	is_left_finished = False
	is_right_finished = False
	if len(left_q) == 1 and len(right_q) == 1:
		sorted_q.append(left_q.pop())
		if sorted_q [0] <= right_q [0]:
			sorted_q.append(right_q.pop())
		else:
			sorted_q.appendleft(right_q.pop())
		return sorted_q
	while len(left_q) != 0 or len(right_q) != 0:
		if len(left_q) == 0:
			print("Left finished: remaining from right", right_q)
			is_left_finished = True
			break
		if len(right_q) == 0:
			print("right finished: remaining from Left", right_q)
			is_right_finished = True
			break

		if left_q [0] == right_q [0]:
			sorted_q.append(left_q.popleft())
			sorted_q.append(right_q.popleft())
		elif left_q [0] < right_q [0]:
			sorted_q.append(left_q.popleft())
		else:
			sorted_q.append(right_q.popleft())

	if is_left_finished:
		while len(right_q) != 0:
			sorted_q.append(right_q.popleft())
	if is_right_finished:
		while len(left_q) != 0:
			sorted_q.append(left_q.popleft())
	return sorted_q


def merge_sort(array_ele):
	"""

	Args:
	 is_heapified:
		array_ele:

	Returns:

	"""
	sorted_q = None
	middle_element_index = len(array_ele) // 2
	# print("-----------")
	# print("Array ele : {} index {}:  len{} ".format(array_ele, middle_element_index, len(array_ele)))
	if len(array_ele) != 1:
		left_q = merge_sort(array_ele [:middle_element_index])
		# print("From left side: ", array_ele)
		print("From left side: ", left_q)
		right_q = merge_sort(array_ele [middle_element_index:])
		# print("From right side: ", array_ele)
		print("From right side: ", right_q)
		sorted_q = sort_two_dequeue(left_q, right_q)
		print("Sorted and merged left and right are : {}", sorted_q)
	else:
		# print("Array Element is 1")
		sorted_q = deque(array_ele)
	# print(sorted_q)
	return sorted_q


if __name__ == '__main__':
	normal_list = [10, 20, 25, 6, 12, 15, 4, 16, 4, -1, 32432]
	# normal_list = [-1, 0, 1, 2, -1, 0, 10]
	print("The unsorted list is : {}".format(normal_list))
	merge_sort(normal_list)
