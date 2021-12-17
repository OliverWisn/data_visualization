# scatter_squares.py
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# Input values for the x and y axes.
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# Setting of the chart style.
plt.style.use("ggplot")

# Generating of the chart.
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Defining of the chart title and axis labels.
ax.set_title("Squares of the numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of the values", fontsize=14)

# Defining of the size of the labels.
ax.tick_params(axis="both", which="major", labelsize=14)

# Chart display.
plt.show()