"""
Insert the elements in the max heap.
"""


# Python Modules
# -N/A

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A


def swift_up(index, max_heap):
	"""
	
	Args:
		index: 

	Returns:

	"""
	if len(max_heap) == 1:
		return

	parent = (index - 1) // 2 if index % 2 == 0 else index // 2
	if max_heap [parent] < max_heap [index]:
		max_heap [parent], max_heap [index] = max_heap [index], max_heap [parent]
		if parent != 0:
			swift_up(parent, max_heap)


if __name__ == '__main__':
	elements = [10, 16, 5, 8, 14, 9, 0, 1, 18]
	maxheap = []
	for _ in elements:
		print("Element to be inserted: {}".format(_))
		maxheap.append(_)
		print("Heap Before insertion :{}".format(maxheap))
		ele_index = maxheap.index(_)
		swift_up(ele_index, maxheap)
		print("Heap After insertion :{}".format(maxheap))
		print("----------")
