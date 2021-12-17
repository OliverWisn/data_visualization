# scatter_squares.py
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# Setting of the chart style.
plt.style.use("ggplot")

# Generating of the chart.
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Defining of the chart title and axis labels.
ax.set_title("Squares of the numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of the values", fontsize=14)

# Defining of the size of the labels.
ax.tick_params(axis="both", which="major", labelsize=14)

# Chart display.
plt.show()