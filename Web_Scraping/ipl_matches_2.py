## Final Data fetching seson wise from the year 2008-2019

import requests
import pandas as pd
from bs4 import BeautifulSoup
from itertools import repeat
from datetime import datetime
import mysql.connector

def scrap(list_,index_,tag,flag=0):
    s = []
    if flag==1:
        for i in list_:
            s.append(list(i.children)[index_].find(tag).text)
        return s
    for i in list_:
        s.append(list(i.children)[index_].find(tag))
        return s

def scrap_attr(list_,index,tag,attr,link=""):
    s = []
    if link == "":
        for i in list_:
            s.append(list(i.children)[index].find(tag).get(attr))
        return s
    for i in list_:
        s.append(link + list(i.children)[index].find(tag)[attr])
    return s


def scrap_child_using_index(list_,list_index,child_index,flag=0):
    s = []
    if flag==1:
        for i in list_:
            s.append(list(list(i.children)[list_index].children)[child_index].text)
        return s
    for i in list_:
        s.append(list(list(i.children)[list_index].children)[child_index])
        return s


year = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
info_date = ['2058','2059','2060','2037','2115','2170','2261','2330','2430','2568','2676','2810','3130']
df = pd.DataFrame()
season = []
matches = []
location = []
links = []
result = []
date = []
for i in range(len(year)):
    url = 'https://www.cricbuzz.com/cricket-series/'+info_date[i]+'/indian-premier-league-'+year[i]+'/matches'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    x = soup.find_all('div',class_='cb-col-75 cb-col')
    matches_ = scrap(x, 0, 'span', flag=1)

    season.extend(repeat(year[i], len(matches_)))
    matches.extend(matches_)
    location.extend(scrap(x, 0, 'div', flag=1))
    links.extend(scrap_attr(x, 0, 'a', 'href', 'https://www.cricbuzz.com'))  # with baselink
    result.extend(scrap_child_using_index(x, 0, 2, flag=1))

    x = soup.find_all('div', class_='cb-col-25 cb-col pad10')
    for i in x:
        fetch_date = int(list(i.children)[0].get('ng-bind')[:11])
        date.append(datetime.fromtimestamp(fetch_date).strftime('%Y-%m-%d %H:%M:%S'))
           
df['season'] = season
df['matches'] = matches
df['location'] = location
df['links'] = links
df['result'] = result
df['date'] = date
df.to_csv("ipl_matches_2.csv", index=False)
