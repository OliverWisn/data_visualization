# sitka_highs.py
# -*- coding: utf-8 -*-

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename =  "data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Downloading of the dates and the maximum temperatures from 
    # the file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Generating the graph of the highest temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")

# Format the plot.
ax.set_title("Highest temperature of the day, July 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

# Plot display.
plt.show()