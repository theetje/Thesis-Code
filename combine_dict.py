"""get_shop_country.py

Author: Thomas de Lange

Code is niet zelf loppend maar is opgezet om hadmatig nieuwe dicts te maken van
een meervoud dict.
"""

# Imports met pp om data te inspecteren. Rest is core voor programma.
from ast import literal_eval
from collections import Counter
from pprint import pprint

base_dict = dict()
new_dict = dict()

# start met een leeg total_counters.txt bestand.
with open('total_counters.txt') as file_:
   base_dict = Counter(literal_eval(file_.read()))

# vul hier in welke je wil optellen bij welken.
with open('data/shop_counter13.txt') as file_:
  new_dict = Counter(literal_eval(file_.read()))

# Output bestand.
with open('total_counters.txt', 'w') as file:
     file.write(str(dict(base_dict + new_dict)))
