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


def merge_sorted_list(sorted_list_1, sorted_list_2):
	"""

	Args:
		sorted_list_1:
		sorted_list_2:

	Returns:

	"""

	j = 0
	i = 0
	len_l1 = len(sorted_list_1)
	len_l2 = len(sorted_list_2)
	sorted_list = []
	while True:
		if l1 [i] < l2 [j]:
			sorted_list.append(l1 [i])
			i += 1
		elif l1 [i] > l2 [j]:
			sorted_list.append(l2 [j])
			j += 1
		elif l1 [i] == l2 [j]:
			sorted_list.append(l1 [i])
			sorted_list.append(l1 [i])
			i = i + 1
			j = j + 1
		if i == len_l1:
			break

		if j == len_l2:
			break

	for _ in range(i, len_l1):
		sorted_list.append(l1 [_])
	for _ in range(j, len_l2):
		sorted_list.append(l2 [_])

	return sorted_list


if __name__ == '__main__':
	l1 = [1, 2, 3, 34, 231, 12, 3, 23, 321, 11, 12, 357, 8]
	l2 = [2, 5, -6, 5, 7, 8, 3, 34, 231, 12, 3, 23, 321, 11, 12, 357, 8]
	l1 = [2, 7, 4, 8]
	l2 = [3, 201, 400, 13, 4]
	print(l1)
	print(l2)
	print(l1.sort())
	print(l2.sort())
	print(l1)
	print(l2)
	sorted_list = merge_sorted_list(l1, l2)
	print(sorted_list)
	print(len(sorted_list))
	print(len(l1) + len(l2))
