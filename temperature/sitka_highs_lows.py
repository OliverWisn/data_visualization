# sitka_highs_lows.py
# -*- coding: utf-8 -*-

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename =  "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Downloading of the dates and the maximum and minimum temperatures 
    # from the file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Generating the plot of the highest temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format the plot.
ax.set_title("Highest and lowest temperature of the day - 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

# Plot display.
plt.show()