# rw_visual.py
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Prepare random walk data and display points.
rw = RandomWalk()
rw.fill_walk()

# Setting of the chart style.
plt.style.use("ggplot")

# Display random walk points.
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.spring, \
    edgecolor="none", s=15)

# Chart display.
plt.show()