from task5 import get_movie_list_details
from pprint import pprint

movie_list = get_movie_list_details

def analyse_movies_language():
    language_dict = {}
    for i in movie_list():
        for r in i["language"]:
            if r in language_dict:
                language_dict[r]+=1
            else:
                language_dict[r]=1
    print(language_dict)
# analyse_movies_language()