#!/usr/bin/env python

from __future__ import print_function
import json
import os
import requests




def get(path, params):
    params = params or {}
    params.update({
        'APPID': os.getenv('OWM_KEY'),
        'units': 'imperial',
    })
    r = requests.get('http://api.openweathermap.org/data/2.5{0}'.format(path),
        params=params)
    return r.json()

data = []
with open('places.json') as fh:
    items = json.load(fh)
    for item in items:
        data.append(get('/forecast', item))

with open('forecast.json', 'w') as fh:
    fh.write(json.dumps({
        'data': data,
    }))



# forecast = get('/forecast', {'q': 'Kanab,us'})

# city = '{0}, {1}'.format(forecast['city']['name'], forecast['city']['country'])
# print(city)
# for item in forecast['list']:
#     rain_chance = item.get('rain', {}).get('3h', 0)
#     clouds = item['clouds']['all']
#     icon = 'http://openweathermap.org/img/w/{icon}.png'.format(icon=item['weather'][0]['icon'])
#     print('{time} low:{low} high:{high} wind:{wind} rain:{rain} {desc}'.format(
#         time=item['dt_txt'],
#         low=item['main']['temp_min'],
#         high=item['main']['temp_max'],
#         wind=item['wind'].get('speed', 0),
#         desc=item['weather'][0]['main'],
#         rain=rain_chance,
#         ))

