"""
Script to calculate second derivative of the given function.
"""
# Python Modules
# -N/A

# 3rd Party Modules
# -N/A

# Project Modules
from derivative import derivative_of_function


# Global Vars
# -N/A


def get_second_derivative(first_derivative):
	return derivative_of_function(first_derivative)


def get_input_function():
	"""
	Sample Input:
	input function: (1/10)*(x**3)
	Enter the value to evaluate:2.5
	"""
	input_function = input("input function: ")
	function_value = float(input("Enter the value to evaluate: "))
	lambda_function = eval("lambda x: {}".format(input_function))
	first_derivative = derivative_of_function(lambda_function)
	second_derivative = get_second_derivative(first_derivative)
	first_derivative_value = first_derivative(function_value)
	second_derivative_value = second_derivative(function_value)
	print(first_derivative_value, second_derivative_value)
	return first_derivative_value, second_derivative_value


if __name__ == '__main__':
	"""
	sample Input:
	input function: (1/10)*(x**3)
	Enter the value to evaluate:2.5
	"""
	print(get_input_function())
