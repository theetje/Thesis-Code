"""get_shop_country.py

Author: Thomas de Lange

Programma gebruikt de api van bing om te zoeken naar het land dat bij de gegeven
lat lng waarde hoord. Deze worden uit een .json bestand gelezen.
"""
import json
from pprint import pprint
import urllib.request

with open('shopname_latlng.json') as file_:
   data = json.load(file_)

country_dict_temp = dict()
bing_key = '?o=json&key=00sO8PiXQLakamNDhkhz~-iA7_W_p_Yy6YSQvIyB2lg~ArpERuu7KrHu92bUv9ZJ0EyKoAqSp7Nq9ma0zJBRy9DFC-OVrmPlTAs7YNst-drn'

for items in data.values():
    print(items)
    # Zoek de waarde van het land op met de bing API
    with urllib.request.urlopen('http://dev.virtualearth.net/REST/v1/Locations/'
                                + items
                                + bing_key) as result:

        info = json.load(result)

        country = info['resourceSets'][0]['resources'][0]['address']['countryRegion']

        if country in country_dict_temp:
            country_dict_temp[country] += 1
        else:
            country_dict_temp[country] = 1

    with open('shop_counter13.txt', 'w') as file:
         file.write(json.dumps(country_dict_temp))
