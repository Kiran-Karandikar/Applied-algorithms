"""
# Docstring.
"""
# Python Modules
from numpy import array, uint8
from numpy.random import randint


# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A


def get_summation_of_values(distribution):
	"""

	Args:
		distribution:

	Returns:

	"""
	total = 0
	for _ in distribution:
		total += _
	return total


def get_mean_of_distribution(distribution):
	"""

	Args:
		distribution:

	Returns:

	"""
	sum_of_values = get_summation_of_values(distribution)
	return sum_of_values / distribution.size


def get_variance_of_distribution(distribution):
	"""

	Args:
		distribution:

	Returns:

	"""
	mean_of_distribution = get_mean_of_distribution(distribution)
	squared_differences = (distribution - mean_of_distribution) ** 2
	return get_summation_of_values(squared_differences) / distribution.size


if __name__ == '__main__':
	data_points = array(randint(0, 100, size=100, dtype=uint8))
	mean = get_mean_of_distribution(data_points)
	variance = get_variance_of_distribution(data_points)
	print(mean, variance)
	print(data_points.mean(), data_points.var())
