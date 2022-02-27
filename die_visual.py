# random_walk.py
# -*- coding: utf-8 -*-

from die import Die

# Creation of the D6 die.
die = Die()

# Perform a number of the throws and list the results.
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)