"""
# Docstring.
"""
# Python Modules
from pprint import pprint


# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A


class Matrices(object):
	def __init__(self, row, col, elements=None):
		self.row = row
		self.col = col
		if elements is not None:
			self.elements = \
				[elements [_:_ + col] for _ in range(0, len(elements), col)]

	def print_all(self):
		if self.elements:
			for _ in self.elements:
				print (_)

	def is_multiplication_possible(self, mat_2):
		return True if self.col == mat_2.row else False

	def total_number_of_calculations(self, mat_2):
		return self.row * self.col * mat_2.col

	def __mul__(self, other):
		all_elements = []
		temp_elements = []
		for _ in self.elements:
			other_row_index = 0
			for ele in _:
				temp_elements.append(
					list(
						map(lambda x: x * ele, other.elements [
							other_row_index]
						    )
					)
				)
				other_row_index += 1
			for _ in range(other.col):
				total_sum = sum(map(lambda x: x [_], temp_elements))
				all_elements.append(total_sum)
			temp_elements = []
		return Matrices(self.row, other.col, all_elements)

	@staticmethod
	def dynamic_programming_matrices_multiplication(p):
		"""
		
		Returns:

		"""
		# Creating dict of p_values for easy access
		p_values = {index: value for index, value in enumerate(p)}
		s_array = {}
		s_array = {i: [0] * len(p) for i in range(2, len(p) + 1)}
		# pprint(s_array)
		# Creating m matrices to store the shortest path
		m_array = {i: [0] * len(p) for i in range(1, len(p))}
		# init second diagonal
		# this will take core of matrix multiplication of just two matrices
		for index in range(1, len(p) - 1):
			m_array.get(index) [index + 1] = \
				p_values [index - 1] * p_values [index] * p_values [index + 1]

		# Since we have already computed two levels:
		# 1. Where i=j i.e [1,1] ... [n,n] =0
		# 2. The multiplication of just two matrices, A1* A2, A2*A3, A(n-1)* An
		total_order = len(p) - 3
		i = 2
		# Here total_order represents total matrices multiplications required
		while total_order != 0:
			total_order -= 1
			j = 1
			next_mat = j + i
			while next_mat <= len(p) - 1:
				required_row = m_array.get(j)
				all_possible_values = {}
				for _ in range(j, next_mat):
					constant_val = p_values [j - 1] * p_values [_] * p_values [
						next_mat]
					all_possible_values [_] = \
						constant_val + m_array.get(j) [_] \
						+ m_array.get(_ + 1) [next_mat]
				required_row [next_mat] = min(all_possible_values.values())
				print(all_possible_values)

				for key in all_possible_values:
					if all_possible_values [key] == required_row [next_mat]:
						print(j, next_mat, _, key)
						s_array.get(next_mat) [j] = key
				j += 1
				next_mat = j + i
			i += 1
		print ("M - array is: -------")
		pprint(m_array)
		print ("Minimum Number of calculations required are:")
		min_cal = m_array.get(1) [len(p) - 1]
		pprint(min_cal)
		return min_cal

	@staticmethod
	def print_parenthesis(s_array, i, j):
		if i == j:
			print ("A{}".format(i))
		else:
			print ("(")
			Matrices.print_parenthesis(s_array, i, s_array.get(j) [i])
			Matrices.print_parenthesis(s_array, s_array.get(j) [i] + 1, j)
			print (")")


if __name__ == '__main__':
	print ("Brute Force Matrices multiplication")
	print ("First Matrix")
	mat_1 = Matrices(2, 3, [1, 2, 3, 4])
	mat_1.print_all()
	print ("Second  Matrix")
	mat_2 = Matrices(3, 2, [9, 10, 8, 11, 7, 12])
	mat_2.print_all()
	mat_3 = Matrices(2, 2, [1, 2, 3, 4])
	print ("Third Matrix is")
	mat_3.print_all()
	mat_4 = Matrices(2, 3, [5, 6, 7, 8, 9, 10])
	print ("Fourth Matrix is")
	mat_4.print_all()
	print ("Matrix Multiplication of 4 matrix by brute force........")
	(mat_1 * mat_2 * mat_3 * mat_4).print_all()

	print ("Dynamic Programming matrices multiplication.......")
	# test cases ordered by number
	p = [4, 10, 3, 12, 20, 7]
	Matrices.dynamic_programming_matrices_multiplication(p)
	p = [4, 10, 3, 12, 20]
	Matrices.dynamic_programming_matrices_multiplication(p)
	p = [4, 10, 3, 12]
	Matrices.dynamic_programming_matrices_multiplication(p)
	p = [4, 10, 3]
	Matrices.dynamic_programming_matrices_multiplication(p)

	p = [30, 35, 15, 5, 10, 20, 25]
	Matrices.dynamic_programming_matrices_multiplication(p)
