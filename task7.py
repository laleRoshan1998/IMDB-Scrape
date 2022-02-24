from task6 import analyse_movies_language, get_movie_list_details
from pprint import pprint

director_list = get_movie_list_details()

def analyse_movies_directors():
    director_dict = {}
    for w in director_list:
        for a in w["director"]:
            if a in director_dict:
                director_dict[a]+=1
            else:
                director_dict[a]=1
    pprint(director_dict)
# analyse_movies_directors()

