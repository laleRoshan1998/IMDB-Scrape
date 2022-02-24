# from asyncio import trsock
# from turtle import position
import json
import requests
from pprint import pprint
from bs4 import BeautifulSoup



# url = "https://www.imdb.com/india/top-rated-indian-movies/"
# pag = requests.get(url)
# soup = BeautifulSoup(pag.text,'html.parser')
# movie_list=[]
# def scrap_top_list():
#     main_div = soup.find('div', class_='lister')
#     tbody = main_div.find('tbody', class_='lister-list')
#     trs = tbody.find_all('tr')
#     movie_ranks = []
#     movie_name = []
#     year_of_realease = []
#     movie_urls = []
#     movie_ratings = []

#     for tr in trs:
#         position = tr.find('td',class_ ="titleColumn").get_text().strip()
#         rank = ''
#         for i in position:
#             if '.' not in i:
#                 rank = rank + i
#             else:
#                 break
#         movie_ranks.append(rank)
#         title = tr.find('td', class_ = "titleColumn").a.get_text()
#         movie_name.append(title)
#         year = tr.find('td', class_ ="titleColumn").span.get_text()
#         year_of_realease.append(year)
#         # imdp_rating = tr.find('td',class_ ="ratingColumn imdprating").strong.get_text()
#         # movie_ratings.append(imdp_rating)
#         link = tr.find('td', class_ ="titleColumn").a['href']
#         movie_link = "https://www.imdp.com" + link
#         movie_urls.append(movie_link)
#     Top_Movie = []
#     details ={'position':'','name':'','year':'','url':''}
#     for i in range(0,len(movie_ranks)):
#         # details['position']=int[movie_ranks[i]]
#         details['name']=str(movie_name[i])
#         year_of_realease[i]=year_of_realease[i][1:5]
#         details['year']=int(year_of_realease[i])
#         # details[rating]=int(movie_ratings[i])
#         details['url']= movie_urls[i]
#         Top_Movie.append(details)
#         details ={'position':'','name':'','year':'','url':''}
#         movie_list.append(details)
#         with open("all_movies.json","w")as var:
#             json.dump(movie_list,var,indent=4)
# pprint(scrap_top_list())


