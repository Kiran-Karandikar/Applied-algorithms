"""
Script to plot function and derivative of function on the matplotlib.
"""
# Python Modules
import matplotlib.pyplot as plt
import numpy as np


# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# -N/A


def derivative_of_function(lambda_function):
	h = 0.00001
	return lambda x: (lambda_function(x + h) - lambda_function(x - h)) / (2 * h)


math_function = lambda x: (1 / 100) * (x ** 3)
data_points = np.linspace(-20, 20, 100)
derivative_values = derivative_of_function(math_function)(data_points)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# spine placement data centered
ax.spines ['left'].set_position(('data', 0.0))
ax.spines ['bottom'].set_position(('data', 0.0))
ax.spines ['right'].set_color('none')
ax.spines ['top'].set_color('none')

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

plt.title("f'(x) and f''(x)")

plt.plot(data_points, math_function(data_points), "r")
plt.plot(data_points, derivative_values, "b")
plt.show()
