import json
from pprint import pprint
from bs4 import BeautifulSoup


with open("all_movies.json","r") as ff:
   data = json.load(ff)

def group_by_decade(movies):
    dict={}
    list = []
    for i in movies:
        yr = i["year"]
        decade=""
        a=0
        for j in str(yr):
            if a==3:
                n=0
                decade+=str(n)
            else:
                decade+=j
                a+=1
            z=decade
        if z not in dict:
            dict[z]=[]
            dict[z].append(i)
        else:
            dict[z].append(i)
        pprint(dict)


# group_by_decade(data)





