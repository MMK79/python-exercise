# import json
# with open("cities.json") as cities_file:
#     cities_data = json.load(cities_file)
#     print(cities_data)

# In a better way 
import json
from pprint import pprint
with open("cities.json") as cities_file:
    cities_data = json.load(cities_file)
    pprint(cities_data)
