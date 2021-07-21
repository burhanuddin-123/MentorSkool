#### Sir guidance
import requests
import pandas as pd
from bs4 import BeautifulSoup

# load webpage into a variable
page = requests.get('https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/matches')

# create a beautifulsoup object and pass on the page content for html parsing
soup = BeautifulSoup(page.content,'html.parser')

x = soup.find_all('div', {'class': 'cb-col-75 cb-col'})  ## also we can pass class_ = 'cb-col-75 cb-col'

df = pd.DataFrame()

# Here and below is column wise extracton taking place
s = []
for i in range(len(x)):
    s.append(list(x[i].children)[0].span.text)
df['match_name'] = s

# Here and below is column wise extracton taking place
s = []
for i in range(len(x)):
    s.append(list(x[i].children)[0].span.text)
df['match_name'] = s

s = []
for i in range(len(x)):
    s.append(list(list(x[i].children)[0].children)[2].text)
df['result'] = s

s = []
for i in range(len(x)):
    s.append('https://www.cricbuzz.com' + (list(x[i].children)[0].a)['href'])
df['link'] = s

df['link'] = df['link'].str.replace('cricket-scores','live-cricket-scorecard')

#storing the dataframe into an Excel sheet
df.to_excel('ipl_2019.xlsx')

