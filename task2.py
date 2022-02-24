import json
from pprint import pprint

with open("all_movies.json","r") as ff:
   data = json.load(ff)

def group_by_year():
    dict={}
    for i in data:
        year = i["year"]
        if year not in dict:
            dict[year]=[]
        else:
            dict[year].append(i)
    pprint(dict)
        

# group_by_year()

