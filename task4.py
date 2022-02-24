
import json,requests
from pprint import pprint
from bs4 import BeautifulSoup



def scrape_movie_details(link):
    reps=requests.get(link)
    soup = BeautifulSoup(reps.text,"html.parser")
    pprint(soup)
    movie_name = soup.find('div',class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.text
    a=[]
    directore_name = soup.find('li',class_="ipc-metadata-list__item").a.text
    a.append(directore_name)
    # print(a)
    country_name = soup.find('li',attrs={'data-testid':"title-details-origin"}).a.text
    # print(country_name)
    language_name = soup.find('li',attrs={'data-testid':"title-details-languages"}).a.text
    # b=[]
    # b.append(language_name)
    # print(b)
    poster_image_link = soup.find('img',class_="ipc-image")['src']
    # print(poster_image_link)
    bio_name = soup.find('span',attrs= {'data-testid':"plot-xs_to_m"}).text
    # print(bio_name)
    runtime_name = soup.find('li',attrs= {'data-testid':"title-techspec_runtime"})
    # print(runtime_name)

    m=runtime_name.find('div',class_="ipc-metadata-list-item__content-container").text
    # print(m)

    run_time = m.replace(" hours", '').replace(" minutes", '').replace(" hour", '').replace(" minute", '').replace(' h',  '').replace('m', '')
    run = run_time.split(" ")
    i = 0
    if len(run)==2:
        i+=int(run[0])*60
        i+=int(run[1])
    elif len(run)==1:
        if "h" in m:
            i+=int(run[0])*60
        else:
            i+=int(run[0])
    # print(i)
    drama_name = soup.find('li',attrs= {'data-testid':"storyline-genres"})
    # print(li)
    ul = drama_name.find('ul',class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base")
    # print(ul)
    y = ul.find_all('li')[0].a.text
    # print(y)
    movies_details={}
    movies_details["name"]= movie_name
    movies_details["directore_name"]= directore_name
    movies_details["country_name"]= country_name
    movies_details["language_name"]= language_name
    movies_details["poster_image_link"]= poster_image_link
    movies_details["i"]= i
    movies_details["y"]= y
    # return movies_details
    pprint(movies_details)
    with open("taks4.json","w") as ll:
        json.dump(movies_details,ll,indent=4)

# pprint (scrape_movie_details("https://www.imdb.com/title/tt0066763/"))
