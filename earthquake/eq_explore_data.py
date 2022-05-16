# eq_explore_data.py
# -*- coding: utf-8 -*-

import json

# Data structure analysis.
filename =  'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Creation of the earthquake list.
all_eq_dicts = all_eq_data['features']

# Mining of the force of the earthquake.
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:20])