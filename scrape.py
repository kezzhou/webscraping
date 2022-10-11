#### Imports ####

import requests

from bs4 import BeautifulSoup

import pandas as pd




#### Healthcare IT News ####

page = requests.get('https://www.healthcareitnews.com/news') ## this is a page we've gotten familiar with as a cohort over the course of the program

## it lists healthcare it news (as its name suggests) in a simple and digestable list format

page 

## creating bs4 object
soup = BeautifulSoup(page.text, 'html.parser')

soup

## cleaning up format and printing
print(soup.prettify())


## retrieving titles
titles = soup.find_all('div', class_='views-field views-field-title')

titlelist = []

for i in titles:
    print(i.text)
    titlelist.append(i.text)

titlelist

len(titlelist) ## we can check our work by checking the length in py and then counting manually on the site

titlelist[1]

titlelist[2]


## author names
authors = soup.find_all('span', class_='author_list')

authorlist = []

for i in authors:
    print(i.text)
    desc = i.text
    desc = desc.strip()
    desc = desc.replace('\n','') ## unlike the other items, the author text has new lines (\n) that need to be removed
    authorlist.append(desc)
authorlist

len(authorlist) ## this should match len of titlelist


## posting times
times = soup.find_all('span', class_='time_list')

timelist = []

for i in times:
    print(i.text)
    timelist.append(i.text)

timelist

len(timelist) ## this should match len of titlelist and authorlist


## posting days
days = soup.find_all('span', class_='day_list')

daylist = []

for i in days:
    print(i.text)
    daylist.append(i.text)

daylist

len(daylist) ## this should match len of titlelist, authorlist, and timelist


## Compiling all the scraped information as a dataframe
df = pd.DataFrame({'article_title':titlelist,'author':authorlist, 'time_posted':timelist, 'day_posted':daylist})

df

df.to_csv('./data/healthcareitnews.csv')





#### Yahoo Finance: Crypto ####

page = requests.get('./yahoofinancecrypto.html') ## this is a page we've gotten familiar with as a cohort over the course of the program

## it lists healthcare it news (as its name suggests) in a simple and digestable list format

page 

## creating bs4 object
with open('/Users/kevinzhou/Documents/GitHub/webscraping/yahoofinancecrypto.html') as x:
    soup = BeautifulSoup(x.text, 'lxml')

soup

## cleaning up format and printing
print(soup.prettify())


## Ticker symbol

days = soup.find_all('a', class_='Fw(600) C($linkColor)')

daylist = []

for i in days:
    print(i.text)
    daylist.append(i.text)

daylist

len(daylist)
















repostars = soup.find_all('a', class_='Link--muted d-inline-block mr-3')

repostars

for i in repostars:
    print('Count:', i.text)

# get the programming language from each repo
p_langauge = soup.find_all('span',attrs={'itemprop': 'programmingLanguage'})
# for each item in p_langauge, print the text

for i in p_langauge:
    print(i.text)


# find each article where class='Box-row'
articles = soup.find_all('article', class_='Box-row')
# get length of articles
len(articles)



# get the div that contains data-hpc
articles = soup.find_all(attrs={"data-hpc":True})  ## way one 
articles = soup.find_all('div',attrs={'data-hpc':True}) ## way two 


### by looking at the website, can see this is where the info is stored: 
# <h1 class=h3 lh-condensed  ---- this is for the name of the repo 
# <p1 class=col-9 color-fg-muted my-1 pr-4 ---- this is for the description of the repo

# get the name of the repo and print it
repo_name = soup.find_all('h1',class_='h3 lh-condensed')

repo_names = []

for item in repo_name:
    print(item.text)
    name = item.text 
    ## clean name remove whitespace
    name = name.strip()
    ## remove new line
    name = name.replace('\n','')
    ## remove all white space
    name = name.replace(' ','')
    repo_names.append(name)
len(repo_names)

repo_names

for names in repo_names:
    print(names)

# get the description of the repo and print it
repo_desc = soup.find_all('p',class_='col-9 color-fg-muted my-1 pr-4')
repo_descs = []
for item in repo_desc:
    print(item.text)
    desc = item.text
    ## clean name remove whitespace
    desc = desc.strip()
    ## remove new line
    desc = desc.replace('\n','')
    repo_descs.append(desc)
len(repo_descs)

repo_descs


## put this together into a dataframe
df = pd.DataFrame({'repo_name':repo_names,'repo_desc':repo_descs})

df

df.to_csv('./trendinggithub.csv')