import requests
import pandas as pd
from bs4 import BeautifulSoup
# from itertools import repeat

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


year = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
info_date = ['2058','2059','2060','2037','2115','2170','2261','2330','2430','2568','2676','2810']
url = 'https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/matches'
page = requests.get(url)

soup = BeautifulSoup(page.content,"html.parser")

x = soup.find_all('div',class_='cb-col-75 cb-col')

df = pd.DataFrame()

df['matches'] = scrap(x,0,'span',flag=1)

df['location'] = scrap(x,0,'div',flag=1)

df['links'] = scrap_attr(x,0,'a','href','https://www.cricbuzz.com') # with baselink

df['links'] = df['links'].str.replace('cricket-scores','live-cricket-scoreboard')

df['result'] = scrap_child_using_index(x,0,2,flag=1)
