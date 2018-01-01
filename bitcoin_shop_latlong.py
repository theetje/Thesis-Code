"""bitcoin_shop_counter.py
Author: Thomas de Lange

Bestand leest data uit van coinmap api: https://coinmap.org/api/v1/venues/
"""

import urllib.request

import json
from pprint import pprint

# Haal alle data op vanuit de coinmap api.
with urllib.request.urlopen('https://coinmap.org/api/v1/venues/') as response:
   data = json.load(response)

# Maak de dict aan waarin de landen worden geteld.
shop_dict_latlng = dict()

# Zet de data om naar lat long values die de google api in een land om zet
for i in range(0, len(data['venues'])):
    latlng = str(data['venues'][i]['lat']) + "," + str(data['venues'][i]['lon'])
    shop_dict_latlng[data['venues'][i]['name']] = latlng

# Laat data in terminal zien en schrijf naar bestand
print(shop_dict_latlng)
with open('shopname_latlng.json', 'w') as file:
     file.write(json.dumps(shop_dict_latlng))
