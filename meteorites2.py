#prend les coordonnées des météorites sur le site nasa et donneles dix plus proches du lieu indiqué

#import des librairies
import math
import requests

#import des données via api et conversion en JSON
meteor_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
#print(meteor_resp.text)

#transfo enJSON en python
meteor_data= meteor_resp.json()
#test conversion par affichage du premier element
#print(meteor_data[0])

print("votre latitude ?")
lat2 = float(input())
print ("longitude ? ")
lon2 = float(input())



#distance de la position aux météorites

import math

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))
    
for meteor in meteor_data:
	if not ('reclat' in meteor and 'reclong' in meteor): continue
	meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']), lat2, lon2)
	#print("distance est de ", meteor['distance'], "km")

def get_dist(meteor):
	#if ('distance' not in meteor): continue
	return meteor.get('distance', math.inf)
	
meteor_data.sort(key=get_dist)

for meteor in meteor_data[0:10]:
	print(meteor['name'], int(meteor['distance']), int(float(meteor['mass'])/1000))