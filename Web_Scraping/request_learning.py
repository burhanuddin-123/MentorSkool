# # https://www.datacamp.com/community/tutorials/web-scraping-using-python - WebScraping
#
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# from openpyxl import Workbook # why this need to be imported
#
# page = requests.get('https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/matches')
# # print(r.text)
# # print(r.content)
#
# soup = BeautifulSoup(page.content,'html.parser')
# # soup = BeautifulSoup(page.content,'html.parser').get_text()
# # print(soup)
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.body)
# # print(soup.head)
# # print(soup.div)
# # print(soup.a)
#
# # link = soup.find_all('a')
# # print(link) # print all <a> tag
# # for x in link:
# #     print(x.get('href'))  # extract links from <a href="">
#
# # x = soup.find_all('div') # extract all <div> tag
# # print(x)
# x = soup.find_all('div',{'class': 'cb-col-75 cb-col'}) # Extract all <div> tag of where class = cb-col-7 cb-col
# # print(x)
#
# df = pd.DataFrame() #creating Empty DataFrame
# # # print(df)
#
# # s.append(list(x[i].children)[0].div.text) # main <div> tag jo extract kiya usme dusre jo div tag hai wo childrean hai aur wo list mein print hota hai ab usme se hum  jisme ek hi element hai aur jo square bracket ke sath print hota hai but agar use without square bracket ke fetch karna hai to [0] use karenge matlab wo list ke [0] element ko fetch karega aur isiliye output mein square bracket print nahi honge, ab mujhe <div> tage chahiye to isiliye mein .div use karunga jisse [0] element wale <div> mein jo bhi <div> tage hai wo fetch hojayenge but with tag aayenge magar agar mujhe uske sirf text ko print karna hai to .text se ham uske text ko fetch kar sakte hai.
# # Example :- <div class="cb-col-75 cb-col"> isko ham find_all se fetch kar rahe hai
# # Now there are 59 <div class="cb-col-75 cb-col"> tag and every of that contains 1 children tag that is
# # <div class=cb-col-60 cb-col cb-srs-mtchs-tm> , Thus to fetch children tag from every <div class="cb-col-75 cb-col">
# # tag we are iterating it into a loop and fetching the child tag through [0]. As without [0] it will be printed in a list..
# #  ab isme children tag ek hi hai jo hai <div class=cb-col-60 cb-col cb-srs-mtchs-tm>
# # ab hame isme se <span> wale tag ko fetch karna hai to we will use .span magar wo <span> tag ke sath fetch hoga
# # to sirf text fetch karne ke liye hame .text use karna padega
#
#
#
# s = [] # creating a list
# for i in range(len(x)):
#     # print(x[i].children)
#     # s.append(list(x[i].children))
#     # s.append(list(x[i].children)[0])
#     s.append(list(x[i].children)[0].span.text)
#
# # for i in s:
# #     print(i)
#
# df['match_name'] = s
# # print(df['match_name'])
#
# #  ab hum iske andar wale div tage jo ki  <div class="text-gray"> hai usko fetch karne ke liye .div use kar rahe hai magar wo <div> tag ke sath aayega
# # uske sirf text ko fetch karna hai to hame .text use karna padega as we have done above
#
# s = []
# for i in range(len(x)):
#     s.append(list(x[i].children)[0].div.text)
# df['location'] = s
# # print(df['location'])
#
# # Now we are fetching chldren of <div class="cb-col-60 cb-col cb-srs-mtchs-tm"> jo ki main <div class="cb-col-75 cb-col> ka child hai.
# # here we are extracting 2 child of <div class="cb-col-60 cb-col cb-srs-mtchs-tm"> using [2] i.e <a> tag
# # to fetch the text we will use .text
# s = []
# for i in range(len(x)):
#     # print((list(x[i].children)[0]))
#     # print(list(list(x[i].children)[0].children)) ## we are fetching children using .children
#     s.append(list(list(x[i].children)[0].children)[2].text)
# df['result'] = s
# # print(df)  # will print [60 rows X 3 columns]
#
# s = []
# for i in range(len(x)):
#     # s.append(list(x[i].children)[0].a) #fetch all <a> tag
#     # s.append(list(x[i].children)[0].a['href']) # fetches the links that is in href of <a> tag
#     s.append('https://www.cricbuzz.com' + (list(x[i].children)[0].a)['href'])
#     # appends the https://www.cricbuzz.com with every links that are fetched
# df['link'] = s
#
# # Now all the links that we have fetched contains cricket-scores ex:-https://www.cricbuzz.com/cricket-scores/22509/mi-vs-csk-final-indian-premier-league-2019
# # but we have to replaced cricket-scores with live-cricket-scoreboard
# df['link'] = df['link'].str.replace('cricket-scores','live-cricket-scoreboard')
#
#
#
#
# # Now after fetching essential records we would store it into excel sheet
# # df.to_excel('ipl_2019.xlsx') # file name is ipl_2019.xlsx
# # df.to_csv('ipl_2019.csv') # file name is ipl_2019.csv
# df.to_csv('ipl_2019.xlsx') # if i use to_excel method then we need to import Workbook from openpyxl
#
#
# ###############################################################3
#
# page = requests.get('https://www.freemaptools.com/how-far-is-it-between.htm')
#
# soup = BeautifulSoup(page.content,"html.parser")
# # print(soup.prettify())
# # exit()
#
# x = soup.find_all('a') #,{'class':'cb-col-75 cb-col'})
# for i in x:
#     if i.get('href') != '#':
#         print(i.get('href'))
# exit()

###############################################################
