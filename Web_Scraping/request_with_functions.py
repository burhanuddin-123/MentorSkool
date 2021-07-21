import requests
import pandas as pd
from bs4 import BeautifulSoup


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


###################################################
## Main
# 2008 ipl link :- https://www.cricbuzz.com/cricket-series/2058/indian-premier-league-2008/matches
# 2009 ipl link :- https://www.cricbuzz.com/cricket-series/2059/indian-premier-league-2009/matches

# page = requests.get('https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2021/matches')
#
# soup = BeautifulSoup(page.content,"html.parser")
#
# x = soup.find_all('div',class_='cb-col-75 cb-col')
#
# df = pd.DataFrame()
#
# df['matches'] = scrap(x,0,'span',flag=1)
# df['location'] = scrap(x,0,'div',flag=1)
# df['links'] = scrap_attr(x,0,'a','href','https://www.cricbuzz.com') # with baselink
#
# df['links'] = df['links'].str.replace('cricket-scores','live-cricket-scoreboard')
#
# df['result'] = scrap_child_using_index(x,0,2,flag=1)
#
# df.to_csv("ipl_2019.csv", index=False) # index=False will remove index in csv file


##################################################################
## Fetching the


