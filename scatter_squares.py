# scatter_squares.py
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# Input values for the x and y axes.
x_values = range(1001)
y_values = [x**2 for x in x_values]

# Setting of the chart style.
plt.style.use("ggplot")

# Generating of the chart.
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.spring, s=10)

# Defining of the chart title and axis labels.
ax.set_title("Squares of the numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of the values", fontsize=14)

# Defining of the size of the labels.
ax.tick_params(axis="both", which="major", labelsize=14)

# Defining the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# Save the chart.
plt.savefig("squares_plot.png", bbox_inches="tight")

# Chart display.
plt.show()