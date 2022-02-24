from importlib.resources import path
import json
from traceback import print_tb
from task4 import scrape_movie_details
from pprint import pprint
import random,time
from os import path


with open ("all_movies.json","r") as var:
    url=json.load(var)
    

def scrape_movies_json():
    time.sleep(random.randint(3,5))
    main_list = []
    for j in url:
        url_name=j["url"]
        file_name="movies/"+url_name[27:36]+".json"
        if path.exists(file_name):
            all_movie = json.load(open(file_name))
        else:
            all_movie=scrape_movie_details(url_name)
            with open(file_name,"w+") as file:
                json.dump(all_movie,file,indent=6)
        main_list.append(all_movie)
    pprint(main_list)
# scrape_movies_json()
        











