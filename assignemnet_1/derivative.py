"""
Script to calculate derivative of the given function.
"""


# Python Modules
# -N/A

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A


def derivative_of_function(lambda_function):
	h = 0.00001
	return lambda x: (lambda_function(x + h) - lambda_function(x - h)) / (2 * h)


def get_input_function():
	"""
	"""
	input_function = input("input function: ")
	function_value = float(input("Enter the value to evaluate: "))
	lambda_function = eval("lambda x: {}".format(input_function))
	derivative_value = derivative_of_function(lambda_function)(function_value)
	return derivative_value


if __name__ == '__main__':
	print(get_input_function())
	"""
	sample Input
	(1/10)*(x**3)
	2.5
	"""
