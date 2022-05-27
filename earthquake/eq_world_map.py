# eq_world_map.py
# -*- coding: utf-8 -*-

import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Data structure analysis.
filename =  'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Creation of the earthquake list.
all_eq_dicts = all_eq_data['features']

# Extracting of the data about the force and the location of 
# the earthquake.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Earthquake map.
data = [{
    'type': 'scattergeo', 
    'lon': lons, 
    'lat': lats,
    'text': hover_texts, 
    'marker': {
        'size': [5*mag for mag in mags], 
        'color': mags, 
        'colorscale': 'Jet', 
        'reversescale': False, 
        'colorbar': {'title': 'Force'}, 
        }, 
    }]
my_layout = Layout(title='Global Earthquakes')

# Visualization of the results.
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="global_earthquakes.html")