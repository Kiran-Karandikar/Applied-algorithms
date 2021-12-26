"""
# Docstring.
"""
# Python Modules
from math import floor

# Project Modules
from insertion_sort import insertion_sort


# 3rd Party Modules
# -N/A

# Global Vars
# -N/A


def bucket_sort(unsorted_list):
	"""

	Args:
		unsorted_list:

	Returns:

	Warnings:
		- The hash function defined in this sort, considers `unsorted_list` is made up of fractions.
	"""
	buckets = [0 for ele in range(0, 10)]
	for ele in unsorted_list:
		bucket = int(floor(ele * len(unsorted_list)))
		if isinstance(buckets [bucket], int):
			buckets [bucket] = []
		buckets [bucket].append(ele)
	for index, bucket in enumerate(buckets):
		if isinstance(buckets [index], list):
			insertion_sort(buckets [index])
	sorted_list = []
	for index, bucket in enumerate(buckets):
		if isinstance(buckets [index], list):
			sorted_list.extend(buckets [index])
	return sorted_list


if __name__ == '__main__':
	unsorted_list = [0.10, 0.16, 0.055, 0.8, 0.14, 0.009, 0, 0.001, 0.118]
	sorted_list = bucket_sort(unsorted_list)
	print(sorted_list)
