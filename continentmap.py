#!/usr/bin/env python
# coding: utf-8
import csv
import json
import sys

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

import geonamescache
gc = geonamescache.GeonamesCache()
geocountries = gc.get_countries()

continents = {}
geocontinents = {}

# use data from http://www.flickr.com/places/
with open('flickr-places-data.json', 'r') as f:
    geocontinents = json.load(f)

if 1 == len(sys.argv):
    print('Usage example:\npython %s EU' % sys.argv[0])
    sys.exit()

contcode = sys.argv[1]
print 'Processing continent: %s' % contcode

with open('data/GeoLiteCity-Location.csv', 'rb') as csvin:
#with open('data/geotest.csv', 'rb') as csvin:
    reader = csv.reader(csvin)
    next(reader)  # copyright notice
    next(reader)  # headings

    for row in reader:
        iso = row[1]
        # records can have 01, AP, EU, A1, A2 as country
        if iso not in geocountries:
            continue

        if contcode != geocountries[iso]['continentcode']:
            continue

        if contcode not in continents:
            continents[contcode] = {'lats': [], 'lons': []}

        continents[contcode]['lats'].append(float(row[5]))
        continents[contcode]['lons'].append(float(row[6]))


geocont = geocontinents[contcode]
m = Basemap(
    projection='mill', lon_0=geocont['lon'], lat_0=geocont['lat'],
    llcrnrlon=geocont['bbox']['w'], llcrnrlat=geocont['bbox']['s'],
    urcrnrlon=geocont['bbox']['e'], urcrnrlat=geocont['bbox']['n'])

# no visible border around map
m.drawmapboundary(fill_color='#ffffff', linewidth=0.0)

cont = continents[contcode]
x, y = m(cont['lons'], cont['lats'])
m.scatter(x, y, 1, marker='.', color='#325CA9')

fig = plt.gcf()
fig.set_alpha(.7)
fig.set_size_inches(36, 24)

plt.savefig('img/%s.png' % contcode, bbox_inches='tight', pad_inches=0.0)