# sitka_highs.py
# -*- coding: utf-8 -*-

import csv

import matplotlib.pyplot as plt

filename =  "data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Downloading of the maximum temperatures from the file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# Plot data.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(highs, c="red")

# Format the plot.
ax.set_title("Highest temperature of the day, July 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

# Plot display.
plt.show()