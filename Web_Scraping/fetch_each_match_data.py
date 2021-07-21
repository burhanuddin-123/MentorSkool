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

page = requests.get('https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/matches')

soup = BeautifulSoup(page.content,"html.parser")



x = soup.find_all('div',class_='cb-col-75 cb-col')

df = pd.DataFrame()
# links = []
# df['matches'] = scrap(x,0,'span',flag=1)
# df['location'] = scrap(x,0,'div',flag=1)
df['links'] = scrap_attr(x,0,'a','href','https://www.cricbuzz.com') # with baselink
df['links'] = df['links'].str.replace('cricket-scores','live-cricket-scorecard')
links = list(df['links'])

# print(links)
# exit()

page = requests.get(links[0])
soup = BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())

# x = soup.find_all('div',class_='cb-col cb-col-100 cb-bg-white')
# x = soup.find_all('div',class_='cb-col cb-col-100 cb-ltst-wgt-hdr')
# x = soup.find_all('div',class_='cb-nav-main cb-col-100 cb-col cb-bg-white')
# x = soup.find_all('div',class_='cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray')
x = soup.find_all('div',class_='cb-col cb-col-100 cb-scrd-itms')  # Final
# x = soup.find_all('div',class_='cb-col cb-col-27')
# x = soup.find_all('div', id = 'innings_1')

# c = 5
# l = 0
# for i in x:
#     if l > 10:
#         break
#     print(list(list(list(i.children)[1].children)[c].children)[5].text) #[1].find('div'))
#     c = c+2
#     l = l+1
# exit()



df_2 = pd.DataFrame()
s = []

for i in x:
    if list(i.children)[1].find('a') == None:
        break
    s.append((list(i.children)[1].find('a').text)) #[1].find_all('div'))
df_2['batsmen'] = s
# exit()


# c = 0
# print("RCB Batsmen:-")
# for i in x:
#     if list(i.children)[1].find('a') == None:
#         break
#     print(list(i.children)[1].find('a').text)  #[].find('div')) # [1].find('div'))
#     c = c+1
s = []
for i in x:
    if i.find('span') == None:
        break
    s.append(i.find('span').text)#.find('div')
df_2['wicket status'] = s

s = []
x = soup.find_all('div',class_='cb-col cb-col-8 text-right text-bold')  # Final
for i in range(1,12):
    s.append(x[i].text)
df_2['Runs'] = s

s = []
x = soup.find_all('div',class_='cb-col cb-col-8 text-right')  # Final
for i in range(4,48,4):
    s.append(x[i].text)
df_2['Balls'] = s

s = []
x = soup.find_all('div',class_='cb-col cb-col-8 text-right')  # Final
for i in range(5,48,4):
    s.append(x[i].text)
df_2['Fours'] = s

s = []
x = soup.find_all('div',class_='cb-col cb-col-8 text-right')  # Final
for i in range(6,48,4):
    s.append(x[i].text)
df_2['Sixes'] = s

s = []
x = soup.find_all('div',class_='cb-col cb-col-8 text-right')  # Final
for i in range(7,48,4):
    s.append(x[i].text)
df_2['SR'] = s

print(df_2)

# print(df_2)

# s = []
# for i in x:
#     print(i.find('div'))


# print("\nRCB Bowler:-")
# for i in range(c,len(x)):
#     if list(x[i].children)[1].find('a') == None:
#         continue
#     print(list(x[i].children)[1].find('a').text)


# df['batsmen'] = scrap(x,1,'a',flag=1)

# df['batsmen'] = scrap(x,1,'div',flag=0)
# print(df['batsmen'])

# df['links'] = df['links'].str.replace('cricket-scores','live-cricket-scorecard')

# df['result'] = scrap_child_using_index(x,0,2,flag=1)

# df.to_csv("ipl_2019.csv", index=False) # index=False will remove index in csv file
