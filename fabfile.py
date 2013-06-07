# coding: utf-8
from fabric.api import local


def git():
    local('git add . && git commit -a')
    local('git push')


def contmaps(continentcode=None):
    continentcodes = ['AF', 'NA', 'OC', 'AN', 'AS', 'EU', 'SA']
    if continentcode:
        continentcodes = [continentcode]

    for cc in continentcodes:
        local('./continentmap.py %s' % cc)


def worldmaps(markersize=None):
    markersizes = [.1, .01, .005]
    if markersize:
        markersizes = [markersize]

    for ms in markersizes:
        local('./worldmap.py %s' % ms)


def maps():
    contmaps()
    worldmaps()