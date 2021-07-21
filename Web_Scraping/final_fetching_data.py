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
    if int(year[i]) <= 2010 :
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

        ###Fatching date
        x = soup.find_all('div', class_='cb-col-25 cb-col pad10')
        for i in x:
            fetch_date = int(list(i.children)[0].get('ng-bind')[:11])
            date.append(datetime.fromtimestamp(fetch_date).strftime('%Y-%m-%d %H:%M:%S'))
            # date.append(list(i.children)[0].get('ng-bind'))
        # date.extend(scrap_attr(x,0,'ng-bind'))
    else:
        url = 'https://www.cricbuzz.com/cricket-series/'+info_date[i]+'/indian-premier-league-'+year[i]+'/matches'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        x = soup.find_all('div', class_='cb-col-75 cb-col')
        matches_ = scrap(x, 0, 'span', flag=1)

        season.extend(repeat(year[i], len(matches_)))
        matches.extend(matches_)
        location.extend(scrap(x, 0, 'div', flag=1))
        links.extend(scrap_attr(x, 0, 'a', 'href', 'https://www.cricbuzz.com'))  # with baselink
        result.extend(scrap_child_using_index(x, 0, 2, flag=1))

        ###Fatching date
        x = soup.find_all('div', class_='cb-col-25 cb-col pad10')
        for i in x:
            fetch_date = int(list(i.children)[0].get('ng-bind')[:11])
            date.append(datetime.fromtimestamp(fetch_date).strftime('%Y-%m-%d %H:%M:%S'))    # <span ng-bind=" 1554215400000| date:'MMM dd, EEE' : '+05:30'">
            # date.append(list(i.children)[0].get('ng-bind'))  # we will use append instead of extend as we are inserting individual element, while extend is used when we have to insert a complete list
        # date.extend(scrap_attr(x, 0, 'ng-bind'))

df['season'] = season
df['matches'] = matches
df['location'] = location
df['links'] = links
df['result'] = result
# print(date)
# print(len(date))
df['date'] = date
df.to_csv("ipl_matches.csv", index=False)




#######################################################################

############# INSERTING DATAFRAME RECORDS INTO SQL

# ## Fetching columns names
# # columns_ = list(df.columns)
# # print(columns_)
#
# # for i in columns_:
# #     print(i)
# # exit()
#
# ## iterate over loop
# # for index,product in df.iterrows():
# #     print(tuple(product))
# # exit()
#
# ## Finding columns Datatype
# # datatypes = list(df.dtypes)
# # print(datatypes)
# #
# # proper_dtype = []
# # for i in datatypes:
# #     if i=="object":
# #         proper_dtype.append("VARCHAR(500)")
# #     elif i=="int64":
# #         proper_dtype.append("INT")
# #     else:
# #         proper_dtype.append("NUMBER")
#
# # print(proper_dtype)
# # exit()
#
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
# )
#
# mycursor = mydb.cursor()
#
# ## Creating a Database
# mycursor.execute("CREATE DATABASE WebScraping")
#
# ## Creating a Table
# ## 1 way --- Static Way
# mycursor.execute("CREATE TABLE WebScraping.IplMatches (season VARCHAR(20), matches VARCHAR(200), location VARCHAR(200), links VARCHAR(2000), result VARCHAR(200))")
#
# ## 2 way --- Dynamic way
# # mycursor.execute(f"CREATE TABLE WebScraping.IplMatches ( {columns[0]} {proper_dtype[0]} )")
# #
# # for i in range(len(columns)):
# #     mycursor.execute(f"ALTER TABLE WebScraping.IplMatches ADD {columns[i]} {proper_dtype[i]}")
# # mycursor.execute("CREATE TABLE WebScraping.IplMatches ")
#
# ## Insert Data
# for index,product in df.iterrows():
#     mycursor.execute(f"INSERT INTO WebScraping.IplMatches VALUES {tuple(product)}")
#
# mydb.commit()
# mydb.close()

###########################################################################


