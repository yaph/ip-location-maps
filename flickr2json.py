# coding: utf-8
import json

geocontinents = {}
with open('flickr-places-data.txt', 'r') as f:
    geocont = f.read()

for rec in geocont.split('\n\n'):
    contcode, bbox, coords = rec.split('\n')
    lat, lon = [float(c.strip()) for c in coords.split('\t')[1].split(',')]
    w, s, e, n = [float(c.strip()) for c in bbox.split('\t')[1].split(',')]

    geocontinents[contcode] = {
        'lat': lat,
        'lon': lon,
        'bbox': {
            'w': w,
            's': s,
            'e': e,
            'n': n
        }
    }

with open('flickr-places-data.json', 'w') as f:
    json.dump(geocontinents, f)