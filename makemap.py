#!/usr/bin/env python
# coding: utf-8
import csv
import math

rows = []
with open('data/GeoLiteCity-Location.csv', 'rb') as csvin:
    reader = csv.reader(csvin)
    next(reader)  # copyright notice
    next(reader)  # headings

    for row in reader:
        if 'US' != row[1]:
            continue
        r = [row[5], row[6]]
        rows.append(r)

# split into chunks of 100000 which tilemill can handle
CHUNK_SIZE = 100000

layers = list(range(0, int(math.ceil(len(rows) / CHUNK_SIZE)) + 1))
for l in layers:
    with open(('iploc%d.csv' % l), 'wb') as csvout:
        writer = csv.writer(csvout)
        writer.writerow(['y', 'x'])  # lon = x, lat = y
        writer.writerows(rows[CHUNK_SIZE * l:CHUNK_SIZE * (l + 1)])

with open('iploc.csv', 'wb') as csvout:
    writer = csv.writer(csvout)
    writer.writerow(['y', 'x'])  # lon = x, lat = y
    writer.writerows(rows)