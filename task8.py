import json
from task4 import scrape_movie_details
from pprint import pprint

with open ("all_movies.json","r") as var:
    url = json.load(var)

def scrape_movie_json():
    for i in url[:10]:
        url_name = i["url"]
        file_name="movies/"+url_name[27:36]+".json"
        all_movies = scrape_movie_details(url_name)
        with open ("file_name","w")as file:
            json.dump(all_movies,file,indent=4)
    # return file_name
    pprint(file_name)

# scrape_movie_json()