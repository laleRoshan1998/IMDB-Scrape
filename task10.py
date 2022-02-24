from task9 import scrape_movies_json
from pprint import pprint

def analyse_language_and_directors():
    movie_json = scrape_movies_json()
    director_dict={}
    for j in movie_json:
        for dire in j["director"]:
            if dire not in director_dict:
                director_dict[dire]={}
                for lan in j["language"]:
                    if lan not in director_dict[dire].keys():
                        director_dict[dire][lan]=1
                    else:
                        director_dict[dire][lan]+=1
    pprint(director_dict)
# analyse_language_and_directors()

