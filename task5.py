import json,requests
# from imdb import Movie
from task4 import scrape_movie_details
from pprint import pprint
from bs4 import BeautifulSoup


with open("all_movies.json","r")as file:
    data=json.load(file)

def get_movie_list_details():
    new_list = []
    for i in data[:10]:
        url=i['url']
        new_list.append(scrape_movie_details(url))
    # return new_list
    print(new_list)
    
# get_movie_list_details()