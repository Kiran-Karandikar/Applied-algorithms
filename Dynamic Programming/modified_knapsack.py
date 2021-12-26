"""
A modified knapsack problem is that for a given set of positive integers a
knap-sack of size s, find a subset A  such that the sum of
elements in A is the largest, but at most s.
Write a program using Python to solve this problem using a top-down
dynamic programming method.

Sample:
	weights = [
		5, 23, 27, 37, 48, 51, 63, 67, 71, 75, 70, 83, 889, 91, 101,
		112, 121, 132, 137, 141, 143, 147, 153, 159, 171, 181, 190, 191
	]
	target_knapsack = 762
"""
# Python Modules

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A

# Store all the sums and respective paths to reach that sum
all_weights = {}


def get_modified_knapsack(
		w_array, index, current_weight, current_node, current_path,
):
	if index == (len(w_array) - 1):
		# current_node included
		all_weights [current_weight + current_node] = "{},{}".format(
			current_path, current_node
		)
		# current_node excluded
		all_weights [current_weight] = current_path
		return
	else:
		index += 1
	# go to include path
	get_modified_knapsack(
		w_array,
		index, current_weight + current_node, w_array [index],
		"{},{}".format(
			current_path, current_node
		)
	)
	# go to exclude path
	get_modified_knapsack(
		w_array,
		index, current_weight, w_array [index],
		current_path
	)


if __name__ == '__main__':
	weights = [
		5, 23, 27, 37, 48, 51, 63, 67, 71, 75, 70, 83, 889, 91, 101,
		112, 121, 132, 137, 141, 143, 147, 153, 159, 171, 181, 190, 191
	]
	target_knapsack = 762
	if len(weights) == 0:
		print ("Weights array is empty")
	elif len(weights) == 1:
		print ("The subset is : {}".format(weights))
	else:
		print ("Generating all knapsacks...")
		get_modified_knapsack(weights, 0, 0, weights [0], "")
		if target_knapsack in all_weights:
			print ("For knapsacks of size :{}".format(target_knapsack))
			print("The subset is : {}".format(all_weights.get(
				target_knapsack
			).lstrip(",")
			                                  ))
		else:
			print ("Target Knapsack not found, Something went wrong .......")
