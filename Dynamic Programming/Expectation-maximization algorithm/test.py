"""
# Docstring.
"""
import os

# Python Modules
import numpy as np
import pandas as pd
from scipy.stats import multivariate_normal as mvn

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
file_name = os.path.join(os.getcwd(), "breastcancer.txt")

if os.path.exists(file_name):
	data = pd.read_csv(file_name, header=None)
	data.replace('?', np.NaN, inplace=True)
	data.dropna(inplace=True)
	prediction_var = data.iloc [:, -1]
	# Get all the required features/columns except the prediction variable and
	# garbage features.
	data = data.iloc [:, 1:10]
	data = np.asarray(data, dtype=float)
	prediction_var_np = np.asarray(prediction_var)
	n, d = data.shape

	###########################################################################
	# Initialize the cluster
	###########################################################################
	# K : number of clusters
	k = 3
	total_iterations = 0
	epsilon = 0.05
	current_epsilon = 1
	# mean for each cluster
	cluster_means = data [np.random.randint(data.shape [0], size=k)]
	# var of each cluster
	cluster_variance = np.zeros((k, d, d), dtype=float)
	for _ in range(k):
		cluster_variance [_] = np.identity(d, dtype=float)
	# Cost function or priori for each cluster
	priori = np.ones((k,), dtype=float) * 1 / float(k)
	w_array = np.zeros((data.shape [0], k), dtype=float)
	# todo - here break when epsilon is greater than said epsilon
	while current_epsilon > 0.0000001:
		total_iterations += 1
		# E - Step
		for _ in range(k):
			w_array [:, _] = mvn.pdf(
				data, cluster_means [_], cluster_variance [_],
				allow_singular=True
			) * priori [_]
		sum_of_all = w_array.sum(axis=1, dtype=float)
		for _ in range(k):
			w_array [:, _] /= sum_of_all

		# Check for the probability
		# for i in range(w_array.shape [0]):
		# 	print (w_array [i, :].sum(axis=0))

		# M - step
		# Multiplying here to force creation of new object
		old_means = cluster_means * 1
		for _ in range(k):
			cluster_sum = w_array [:, _].sum(dtype=float)
			priori [_] = cluster_sum / n
			numerator = (w_array [:, _] * data.T).T.sum(dtype=float, axis=0)
			cluster_means [_] = numerator / cluster_sum
			# Variance Calculation
			_var = w_array [:, _] * (data - cluster_means [_]).T
			cluster_variance [_] = np.dot(
				_var, (data - cluster_means [_])
			).sum(dtype=float) / cluster_sum
			print (cluster_variance [_])
		# this step can be wrong....
		# cluster_variance = cluster_variance * np.identity(d, dtype=float)
		current_epsilon = ((cluster_means - old_means) ** 2).sum(dtype=float)
		print (
			"--------------------------------------------------------------")

		print (current_epsilon, total_iterations)
	print (cluster_means)

# return here total number of iterations
