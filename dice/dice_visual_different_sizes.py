# dice_visual_different_sizes.py
# -*- coding: utf-8 -*-

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Creation of the two D6 dice.
die_1 = Die()
die_2 = Die(10)

# Perform a number of the throws and list the results.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analysis of the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualization of the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of the occurrence of the values"}
my_layout = Layout(title=\
    "Result of the rolling of the two dice - 6-sided die and 10-sided die"+\
    " the fifty thousand times",xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d6_d10.html")