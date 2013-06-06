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
        print(cc)
        #local('python continentmaps.py %s' % cc)