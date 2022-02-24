from task9 import scrape_movies_json
from pprint import pprint

def analyse_movies_genre():
    movie_genre=scrape_movies_json()
    genre_dict={}
    for g in movie_genre:
        for f in g["genre"]:
            if f in genre_dict:
                genre_dict[f]+=1
            else:
                genre_dict[f]=1
    pprint(genre_dict)
# analyse_movies_genre()