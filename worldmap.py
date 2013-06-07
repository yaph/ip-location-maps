#!/usr/bin/env python
# coding: utf-8
import csv
import sys

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

if 1 == len(sys.argv):
    print('Usage example:\npython %s .005' % sys.argv[0])
    sys.exit()

markersize = float(sys.argv[1])

lats = []
lons = []

with open('data/GeoLiteCity-Location.csv', 'rb') as csvin:
    reader = csv.reader(csvin)
    next(reader)  # copyright notice
    next(reader)  # headings

    for row in reader:
        lats.append(float(row[5]))
        lons.append(float(row[6]))

m = Basemap(projection='mill', lon_0=0, lat_0=0)

# no visible border around map
m.drawmapboundary(fill_color='#ffffff', linewidth=0.0)

x, y = m(lons, lats)
m.scatter(x, y, markersize, marker='.', color='#325CA9')

fig = plt.gcf()
fig.set_alpha(.7)
fig.set_size_inches(36, 24)

plt.savefig(
    'img/world%s.png' % str(markersize), bbox_inches='tight', pad_inches=0
)