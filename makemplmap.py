#TODO Bouning boxes for continents
# http://api.geonames.org/getJSON?formatted=true&geonameId=6255146&username=rgmz

import csv

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

lats = []
lons = []

with open('data/GeoLiteCity-Location.csv', 'rb') as csvin:
#with open('geotest.csv', 'rb') as csvin:
    reader = csv.reader(csvin)
    next(reader)  # copyright notice
    next(reader)  # headings

    for row in reader:
#        if row[1] != 'ES':
        #if row[1] != 'US':
            #continue
        lats.append(float(row[5]))
        lons.append(float(row[6]))

#m = Basemap(projection='mill', lon_0=0.53, lat_0=41.39,
    #llcrnrlon=-18, llcrnrlat=27, urcrnrlon=4.33, urcrnrlat=44)  #spain
#    llcrnrlon=-177.1, llcrnrlat=-61.48, urcrnrlon=13.71, urcrnrlat=76.63)  #us

# north america
#m = Basemap(
    #projection='mill', lon_0=-109.7547, lat_0=44.3308,
    #llcrnrlon=-167.2764, llcrnrlat=5.4995,
    #urcrnrlon=-52.2330, urcrnrlat=83.1621)

# Europe
m = Basemap(
    projection='mill', lon_0=7.8578, lat_0=52.9762,
    llcrnrlon=-31.2660, llcrnrlat=27.6363,
    urcrnrlon=39.8693, urcrnrlat=81.0088)

x, y = m(lons, lats)
m.scatter(x, y, 1, marker='.', color='#325C59')
fig = plt.gcf()
fig.set_alpha(.7)
fig.set_size_inches(36, 24)
plt.savefig('img/ipmap-europe.png', bbox_inches='tight', pad_inches=0)