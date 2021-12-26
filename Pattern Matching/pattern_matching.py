"""
# Docstring.
"""
# Python Modules
import string
import time
from pprint import pprint
from random import choice, seed

from matplotlib import pyplot as plt

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# set random seed so you will always get the same random_string
seed(100)
generate_random_strings = lambda letters, size: ''.join(
	choice(letters) for i in range(size)
)


def perform_experiment(func):
	def inner_call(*arg, **kargs):
		start_time = time.time()
		print (func.__name__)
		return_value = func(*arg, **kargs)
		end_time = time.time()
		total_time = end_time - start_time
		return total_time, \
		       return_value.get("all_occurrences"), \
		       return_value.get("total_comparisons"), len(arg [0]), \
		       len(arg [1])

	return inner_call


@perform_experiment
def find_brute(T, P):
	n, m = len(T), len(P)
	all_occurrences = 0
	total_comparisons = 0
	# every starting position
	i = 0
	while i < (n - m) + 1:
		k = 0
		# conduct O(k) comparisons
		while k < m and T [i + k] == P [k]:
			total_comparisons += 1
			k += 1
		if k == m:
			all_occurrences += 1
			i = i + k
		i = i + 1
	return {
		"all_occurrences": all_occurrences,
		"total_comparisons": total_comparisons
	}


# Boyer-Moore
@perform_experiment
def find_boyer_moore(T, P):
	all_occurrences = 0
	total_comparisons = 0
	n, m = len(T), len(P)
	if m == 0:
		return 0
	last = {}
	for k in range(m):
		last [P [k]] = k
	i = m - 1
	k = m - 1
	while i < n:
		# If matched, decrease i,k
		if T [i] == P [k]:
			if k == 0:
				all_occurrences += 1
				k = m - 1
				i += 2 * k
			else:
				i -= 1
				k -= 1
		# Not match, reset the positions
		else:
			j = last.get(T [i], -1)
			i += m - min(k, j + 1)
			k = m - 1
		total_comparisons += 1
	return {
		"all_occurrences": all_occurrences,
		"total_comparisons": total_comparisons
	}


# KMP failure function
def compute_kmp_fail(P):
	m = len(P)
	fail = [0] * m
	j = 1
	k = 0
	while j < m:
		if P [j] == P [k]:
			fail [j] = k + 1
			j += 1
			k += 1
		elif k > 0:
			k = fail [k - 1]
		else:
			j += 1
	return fail


# KMP
@perform_experiment
def find_kmp(T, P):
	all_occurrences = 0
	total_comparisons = 0
	n, m = len(T), len(P)
	if m == 0:
		return 0
	fail = compute_kmp_fail(P)
	j = 0
	k = 0
	while j < n:
		if T [j] == P [k]:
			if k == m - 1:
				all_occurrences += 1
				k = -1
			j += 1
			k += 1
		elif k > 0:
			k = fail [k - 1]
		else:
			j += 1
		total_comparisons += 1
	return {
		"all_occurrences": all_occurrences,
		"total_comparisons": total_comparisons
	}


# Play with letter_set
# letter_set = "ATGC"
letter_set = string.ascii_letters
random_string = generate_random_strings(letter_set, 10 ** 7)
pattern = generate_random_strings("ATGC", 100)

random_string = "onioniononions"
pattern = "onion"
random_string = "ABCDEF"
pattern = "ABC"
# append pattern to the end of string
test_string = random_string + pattern
pprint(find_brute(test_string, pattern))
pprint(find_boyer_moore(test_string, pattern))
pprint(find_kmp(test_string, pattern))

letter_set = string.ascii_letters
data_size = []
total_comparisons_bm = []
execution_times_bm = []
total_comparisons_kmp = []
execution_times_kmp = []
total_comparisons_brute = []
execution_times_brute = []
for i in range(0, 7):
	random_string = generate_random_strings(letter_set, 10 ** i)
	pattern = generate_random_strings("ATGC", 100)
	data_size.append(i)
	# append pattern to the end of string
	test_string = random_string + pattern
	values = find_boyer_moore(test_string, pattern)
	execution_time = values [0]
	total_matches = values [1]
	total_comparison = values [2]
	execution_times_bm.append(execution_time)
	total_comparisons_bm.append(total_comparison)

	values = find_kmp(test_string, pattern)
	execution_time = values [0]
	total_matches = values [1]
	total_comparison = values [2]
	execution_times_kmp.append(execution_time)
	total_comparisons_kmp.append(total_comparison)

	values = find_brute(test_string, pattern)
	execution_time = values [0]
	total_matches = values [1]
	total_comparison = values [2]
	execution_times_brute.append(execution_time)
	total_comparisons_brute.append(total_comparison)

with plt.style.context('Solarize_Light2'):
	plt.plot(data_size, total_comparisons_bm, label="total comparisons",
	         linestyle="-"
	         )
	plt.figtext(0.5, 0.01, "Data size is power of 10", ha="center",
	            fontsize=18,
	            bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5}
	            )
	plt.title('Boyer_moore')
	plt.legend()
	plt.show()
with plt.style.context('Solarize_Light2'):
	plt.plot(data_size, execution_times_bm, label="execution_time",
	         linestyle="-"
	         )
	plt.figtext(0.5, 0.01, "Data size is power of 10", ha="center",
	            fontsize=18,
	            bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5}
	            )
	plt.title('Boyer_moore')
	plt.legend()
	plt.show()
with plt.style.context('Solarize_Light2'):
	plt.plot(data_size, total_comparisons_kmp, label="total comparisons",
	         linestyle="-"
	         )
	plt.figtext(0.5, 0.01, "Data size is power of 10", ha="center",
	            fontsize=18,
	            bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5}
	            )
	plt.title('KMP')
	plt.legend()
	plt.show()
with plt.style.context('Solarize_Light2'):
	plt.plot(data_size, execution_times_kmp, label="execution_time",
	         linestyle="-"
	         )
	plt.figtext(0.5, 0.01, "Data size is power of 10", ha="center",
	            fontsize=18,
	            bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5}
	            )
	plt.title('KMP')
	plt.legend()
	plt.show()

with plt.style.context('Solarize_Light2'):
	plt.plot(data_size, total_comparisons_brute, label="total comparisons",
	         linestyle="-"
	         )
	plt.figtext(0.5, 0.01, "Data size is power of 10", ha="center",
	            fontsize=18,
	            bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5}
	            )
	plt.title('Brute Force')
	plt.legend()
	plt.show()
with plt.style.context('Solarize_Light2'):
	plt.plot(data_size, execution_times_brute, label="execution_time",
	         linestyle="-"
	         )
	plt.figtext(0.5, 0.01, "Data size is power of 10", ha="center",
	            fontsize=18,
	            bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5}
	            )
	plt.title('Brute Force')
	plt.legend()
	plt.show()
