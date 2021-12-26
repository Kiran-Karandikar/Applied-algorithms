"""
# Docstring.
"""
import os
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Python Modules
from scipy.stats import multivariate_normal as mvn

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
###############################################################################
# file_name = os.path.join(os.getcwd(), "breastcancer.txt")
# df = pd.read_csv(file_name, header=None)
# df.replace('?', np.NaN, inplace=True)
# df.dropna(inplace=True)
# prediction_var = df.iloc [:, -1]
# # Get all the required features/columns except the prediction variable
# # and garbage features.
# data = df.iloc [:, 1:10]
# data = np.asarray(data, dtype=float)
# prediction_var_np = np.asarray(prediction_var)
# n, d = data.shape


##############################################################################
# file_name = os.path.join(os.getcwd(), "ionosphere.data")
# df = pd.read_csv(file_name, header=None)
# df.replace('', np.NaN, inplace=True)
# df.dropna(inplace=True)
# prediction_var = df.iloc [:, -1]
# # Get all the required features/columns except the prediction variable and
# # garbage features.
# data = df.iloc [:, 0:df.shape [1] - 1]
# data = np.asarray(data, dtype=float)
# prediction_var_np = np.asarray(prediction_var)
# n, d = data.shape

##############################################################################
file_name = os.path.join(os.getcwd(), "ringnorm.data")
df = pd.read_csv(file_name, header=None, sep="\s+")
df.replace('', np.NaN, inplace=True)
df.dropna(inplace=True)
prediction_var = df.iloc [:, -1]
# Get all the required features/columns except the prediction variable and
# garbage features.
data = df.iloc [:, 0:df.shape [1] - 1]
data = np.asarray(data, dtype=float)
prediction_var_np = np.asarray(prediction_var)
n, d = data.shape


def em_algo(k, epsilon):
	###########################################################################
	# Initialize the cluster
	###########################################################################
	# K : number of clusters
	total_iterations = 0
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
	while current_epsilon > epsilon:
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
		old_means = cluster_means / 1
		for _ in range(k):
			cluster_sum = w_array [:, _].sum(dtype=float)
			priori [_] = cluster_sum / n
			numerator = np.dot(w_array [:, _], data).sum(dtype=float, axis=0)
			cluster_means [_] = numerator / cluster_sum
			# Variance Calculation
			_var = w_array [:, _] * (data - cluster_means [_]).T
			cluster_variance [_] = \
				np.dot(
					_var, (data - cluster_means [_])
				).sum(dtype=float) / cluster_sum
			# this step can be wrong....
			cluster_variance [_] = \
				cluster_variance [_] * np.identity(d, dtype=float)
		current_epsilon = ((cluster_means - old_means) ** 2).sum(dtype=float)
	good_cluster = np.asarray(
		(df [prediction_var == 0]).iloc [:, 0: df.shape [1] - 1], dtype=float
	)
	bad_cluster = np.asarray(
		(df [prediction_var == 1]).iloc [:, 0: df.shape [1] - 1], dtype=float
	)

	# good_cluster = np.asarray(
	# 	(df [prediction_var == 2]).iloc [:, 1:10], dtype=float
	# )
	# bad_cluster = np.asarray(
	# 	(df [prediction_var == 4]).iloc [:, 1: 10], dtype=float
	# )

	for _ in range(k):
		print ("----------+++++++++++++++++++++++------------------------")
		print (np.linalg.norm(cluster_means [_] - good_cluster.mean(axis=0)))
		print (np.linalg.norm(cluster_means [_] - bad_cluster.mean(axis=0)))
	return total_iterations


def perform_experiment(k, n_times):
	all_execution_times = []
	all_iterations_times = []
	for _k in k:
		execution_times = []
		iteration_counter = []
		for _ in range(n_times):
			start_time = time.time()
			iterations = em_algo(_k, 0.0000000001)
			execution_times.append(time.time() - start_time)
			iteration_counter.append(iterations)
		all_execution_times.append(execution_times)
		all_iterations_times.append(iterations)

	data = pd.DataFrame(all_iterations_times)
	data1 = pd.DataFrame(all_execution_times)
	data1.index += 2
	bp = plt.boxplot(data1, patch_artist=True, vert=False)
	for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
		plt.setp(bp [element], color='red')
	for patch in bp ['boxes']:
		patch.set(facecolor="tan")
	plt.subplots_adjust(bottom=0.25)
	plt.yticks([2, 3, 4, 5], ["2", "3", "4", "5"], rotation=15)
	plt.ylabel("Number of clusters")
	plt.xlabel("Execution time in milli seconds")
	plt.show()

	bp = plt.boxplot(data, patch_artist=True, vert=False)
	for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
		plt.setp(bp [element], color='red')
	for patch in bp ['boxes']:
		patch.set(facecolor="tan")
	plt.subplots_adjust(bottom=0.25)
	plt.yticks([2, 3, 4, 5], ["2", "3", "4", "5"], rotation=15)
	plt.ylabel("Number of clusters")
	plt.xlabel("Number of Iterations")
	plt.show()


perform_experiment([2, 3, 4, 5], 20)
