# sitka_highs.py
# -*- coding: utf-8 -*-

import csv

filename =  "data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Downloading of the maximum temperatures from the file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

    print(highs)