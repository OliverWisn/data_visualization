# random_walk.py
# -*- coding: utf-8 -*-

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

print(frequencies)