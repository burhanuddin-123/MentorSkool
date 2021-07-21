# year = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
# info_date = ['2058','2059','2060','2037','2115','2170','2261','2330','2430','2568','2676','2810']
# name = ''
# # year = 2008
# # info_data = 2058
# # info_data_1 = 2037
# for i in range(len(year)):
#     if int(year[i]) <= 2010 :
#         # info_data = 2058
#         url = 'https://www.cricbuzz.com/cricket-series/'+info_date[i]+'/indian-premier-league-'+year[i]+'/matches'
#         print(url)
#         # year = year+1
#         # info_data = info_data + 1
#     else:
#         url = 'https://www.cricbuzz.com/cricket-series/'+info_date[i]+'/indian-premier-league-'+year[i]+'/matches'
#         print(url)
#         # year = year+1
#         # info_data_1 = info_data_1 + 1
#     # year = year + 1
# exit()


########################################################################
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
#
#
# def scrap(s,list_,index_,tag,flag=0):
#     # s = []
#     if flag==1:
#         for i in list_:
#             s.append(list(i.children)[index_].find(tag).text)
#         return s
#     for i in list_:
#         s.append(list(i.children)[index_].find(tag))
#         return s
#
# def scrap_attr(s,list_,index,tag,attr,link=""):
#     # s = []
#     if link == "":
#         for i in list_:
#             s.append(list(i.children)[index].find(tag).get(attr))
#         return s
#     for i in list_:
#         s.append(link + list(i.children)[index].find(tag)[attr])
#     return s
#
#
# def scrap_child_using_index(s,list_,list_index,child_index,flag=0):
#     # s = []
#     if flag==1:
#         for i in list_:
#             s.append(list(list(i.children)[list_index].children)[child_index].text)
#         return s
#     for i in list_:
#         s.append(list(list(i.children)[list_index].children)[child_index])
#         return s
#
#
# year = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
# info_date = ['2058','2059','2060','2037','2115','2170','2261','2330','2430','2568','2676','2810']
# df = pd.DataFrame()
# matches = []
# locations = []
# links = []
# results = []
# for i in range(len(year)):
#     if int(year[i]) <= 2010 :
#         url = 'https://www.cricbuzz.com/cricket-series/'+info_date[i]+'/indian-premier-league-'+year[i]+'/matches'
#         page = requests.get(url)
#         soup = BeautifulSoup(page.content,"html.parser")
#         x = soup.find_all('div',class_='cb-col-75 cb-col')
#
#         links = scrap(links,x,0,'span',flag=1)
#
#         # if i==0:
#         #     df['matches'] = scrap(x,0,'span',flag=1)
#         # else:
#         #     df['matches'].loc[len(df['matches'])] = scrap(x,0,'span',flag=1)
#         # df['matches'] = scrap(x,0,'span',flag=1)
#         # df['location'] = scrap(x,0,'div',flag=1)
#         # df['links'] = scrap_attr(x,0,'a','href','https://www.cricbuzz.com') # with baselink
#         # df['result'] = scrap_child_using_index(x,0,2,flag=1)
#     else:
#         url = 'https://www.cricbuzz.com/cricket-series/'+info_date[i]+'/indian-premier-league-'+year[i]+'/matches'
#         page = requests.get(url)
#         soup = BeautifulSoup(page.content, "html.parser")
#         x = soup.find_all('div', class_='cb-col-75 cb-col')
#
#         links = scrap(links,x,0,'span',flag=1)
#         # df['matches'].loc[len(df['matches'])] = scrap(x,0,'span',flag=1)
#
#         # df['matches'] = scrap(x, 0, 'span', flag=1)
#         # df['location'] = scrap(x, 0, 'div', flag=1)
#         # df['links'] = scrap_attr(x, 0, 'a', 'href', 'https://www.cricbuzz.com')  # with baselink
#         # df['result'] = scrap_child_using_index(x, 0, 2, flag=1)
#
# # print(links)
# df['matches'] = links
# print(df['matches'])
# # df.to_csv("ipl_2019.csv", index=False)  # index=False will remove index in csv file

######################################################################

# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# from itertools import repeat
#
# def scrap(s,list_,index_,tag,flag=0):
#     if flag==1:
#         for i in list_:
#             s.append(list(i.children)[index_].find(tag).text)
#         return s
#     for i in list_:
#         s.append(list(i.children)[index_].find(tag))
#         return s
#
# def scrap_attr(s,list_,index,tag,attr,link=""):
#     if link == "":
#         for i in list_:
#             s.append(list(i.children)[index].find(tag).get(attr))
#         return s
#     for i in list_:
#         s.append(link + list(i.children)[index].find(tag)[attr])
#     return s
#
#
# def scrap_child_using_index(s,list_,list_index,child_index,flag=0):
#     if flag==1:
#         for i in list_:
#             s.append(list(list(i.children)[list_index].children)[child_index].text)
#         return s
#     for i in list_:
#         s.append(list(list(i.children)[list_index].children)[child_index])
#         return s
#
#
# year = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
# info_date = ['2058','2059','2060','2037','2115','2170','2261','2330','2430','2568','2676','2810']
# df = pd.DataFrame()
# season = []
# matches = []
# location = []
# links = []
# result = []
# for i in range(len(year)):
#     if int(year[i]) <= 2010 :
#         url = 'https://www.cricbuzz.com/cricket-series/'+info_date[i]+'/indian-premier-league-'+year[i]+'/matches'
#         page = requests.get(url)
#         soup = BeautifulSoup(page.content,"html.parser")
#         x = soup.find_all('div',class_='cb-col-75 cb-col')
#         matches = scrap(matches,x, 0, 'span', flag=1)
#         empty = []
#         empty = scrap(empty,x, 0, 'span', flag=1)  # to fetch year but this is not that much useful as it
#         # makes processing time longer as without any need we are calling the function...
#         # year_value = year[i]
#         season.extend(repeat(year[i],len(empty)))
#         # print(len(matches))
#         # print(len(season))
#         # print(season)
#         # exit()
#         # season.append(year[i])
#         # season = season * len(matches)
#         # season = season.append(repeat(year[i],len(matches)))
#         # print(len(matches))
#         # print(year[i])
#         # print(year[i] * len(matches))
#         # season = list(year[i] * len(matches))
#         location = scrap(location,x, 0, 'div', flag=1)
#         links = scrap_attr(links,x, 0, 'a', 'href', 'https://www.cricbuzz.com')  # with baselink
#         result = scrap_child_using_index(result,x, 0, 2, flag=1)
#     else:
#         url = 'https://www.cricbuzz.com/cricket-series/'+info_date[i]+'/indian-premier-league-'+year[i]+'/matches'
#         page = requests.get(url)
#         soup = BeautifulSoup(page.content, "html.parser")
#         x = soup.find_all('div', class_='cb-col-75 cb-col')
#         matches = scrap(matches, x, 0, 'span', flag=1)
#         empty = []
#         empty = scrap(empty, x, 0, 'span', flag=1)
#         season.extend(repeat(year[i], len(empty)))
#         # season.append(year[i])
#         # season = season * len(matches)
#         location = scrap(location, x, 0, 'div', flag=1)
#         links = scrap_attr(links, x, 0, 'a', 'href', 'https://www.cricbuzz.com')  # with baselink
#         result = scrap_child_using_index(result, x, 0, 2, flag=1)
#
# # print(len(matches))
# # print(len(season))
# # print(season)
# # exit()
# df['season'] = season
# df['matches'] = matches
# df['location'] = location
# df['links'] = links
# df['result'] = result
# # print(df)
# df.to_csv("ipl_matches.csv", index=False)

################################################################
### COMPLETED ------- DONE

# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# from itertools import repeat
#
# def scrap(s,list_,index_,tag,flag=0):
#     if flag==1:
#         for i in list_:
#             s.append(list(i.children)[index_].find(tag).text)
#         return s
#     for i in list_:
#         s.append(list(i.children)[index_].find(tag))
#         return s
#
# def scrap_attr(s,list_,index,tag,attr,link=""):
#     if link == "":
#         for i in list_:
#             s.append(list(i.children)[index].find(tag).get(attr))
#         return s
#     for i in list_:
#         s.append(link + list(i.children)[index].find(tag)[attr])
#     return s
#
#
# def scrap_child_using_index(s,list_,list_index,child_index,flag=0):
#     if flag==1:
#         for i in list_:
#             s.append(list(list(i.children)[list_index].children)[child_index].text)
#         return s
#     for i in list_:
#         s.append(list(list(i.children)[list_index].children)[child_index])
#         return s
#
#
# year = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
# info_date = ['2058','2059','2060','2037','2115','2170','2261','2330','2430','2568','2676','2810']
# df = pd.DataFrame()
# season = []
# matches = []
# location = []
# links = []
# result = []
# for i in range(len(year)):
#     if int(year[i]) <= 2010 :
#         url = 'https://www.cricbuzz.com/cricket-series/'+info_date[i]+'/indian-premier-league-'+year[i]+'/matches'
#         page = requests.get(url)
#         soup = BeautifulSoup(page.content,"html.parser")
#         x = soup.find_all('div',class_='cb-col-75 cb-col')
#         matches = scrap(matches,x, 0, 'span', flag=1)
#         empty = []
#         empty = scrap(empty,x, 0, 'span', flag=1)
#         season.extend(repeat(year[i],len(empty)))
#         location = scrap(location,x, 0, 'div', flag=1)
#         links = scrap_attr(links,x, 0, 'a', 'href', 'https://www.cricbuzz.com')  # with baselink
#         result = scrap_child_using_index(result,x, 0, 2, flag=1)
#     else:
#         url = 'https://www.cricbuzz.com/cricket-series/'+info_date[i]+'/indian-premier-league-'+year[i]+'/matches'
#         page = requests.get(url)
#         soup = BeautifulSoup(page.content, "html.parser")
#         x = soup.find_all('div', class_='cb-col-75 cb-col')
#         matches = scrap(matches, x, 0, 'span', flag=1)
#         empty = []
#         empty = scrap(empty, x, 0, 'span', flag=1)
#         season.extend(repeat(year[i], len(empty)))
#         location = scrap(location, x, 0, 'div', flag=1)
#         links = scrap_attr(links, x, 0, 'a', 'href', 'https://www.cricbuzz.com')
#         result = scrap_child_using_index(result, x, 0, 2, flag=1)
# df['season'] = season
# df['matches'] = matches
# df['location'] = location
# df['links'] = links
# df['result'] = result
# df.to_csv("ipl_matches.csv", index=False)
#

##################################################################
