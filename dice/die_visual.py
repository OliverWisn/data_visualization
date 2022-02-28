# random_walk.py
# -*- coding: utf-8 -*-

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Creation of the D6 die.
die = Die()

# Perform a number of the throws and list the results.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analysis of the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualization of the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of the occurrence of the values"}
my_layout = Layout(title=\
    "Result of the rolling of the single 6-sided die the thousand times",\
     xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d6.html")