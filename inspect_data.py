from ast import literal_eval
from pprint import pprint
from collections import OrderedDict

with open('total_counters.txt') as file_:
   data = literal_eval(file_.read())

pprint(sorted(data.items(), key=lambda x: x[1]))

total_shops = 0
for items in data.values():
    total_shops += items

print("total_shops: ")
print(total_shops)
