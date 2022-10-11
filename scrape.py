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





#### Coin Market Cap: Cryptocurrency ####

page = requests.get('https://coinmarketcap.com/all/views/all/') ## this is one of many popular websites used for tracking cryptocurrency movement

page 

## creating bs4 object
soup = BeautifulSoup(page.text, 'html.parser')

soup

## cleaning up format and printing
print(soup.prettify())


## Name of coin!

names = soup.find_all('a', class_='cmc-table__column-name--name cmc-link')

namelist = []

for i in names:
    print(i.text)
    namelist.append(i.text)

namelist

len(namelist) ## unfortunately this isn't the full length of the list of coins because there is a loadmore function built into the site
## however, this is always the default number of coins printed on the front page. This len should stay consistent as we look for other items like ticker and price movement


## Ticker Symbol

tickers = soup.find_all('td', class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--hide-sm cmc-table__cell--sort-by__symbol')

tickerlist = []

for i in tickers:
    print(i.text)
    tickerlist.append(i.text)

tickerlist

len(tickerlist) ## matches the number of coin names - so far so good


## Market Cap

marketcaps = soup.find_all('span', class_='sc-1ow4cwt-1 ieFnWP')

marketcaplist = []

for i in marketcaps:
    print(i.text)
    marketcaplist.append(i.text)

marketcaplist

len(marketcaplist)


## Price

prices = soup.find_all('div', class_='sc-131di3y-0 cLgOOr')

pricelist = []

for i in prices:
    print(i.text)
    pricelist.append(i.text)

pricelist

len(pricelist)


## Percent Change within the Hour

changes = soup.find_all('td', class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h')

changelist = []

for i in changes:
    print(i.text)
    changelist.append(i.text)

changelist

len(changelist)


## Putting it all together

cmcdf = pd.DataFrame({'coin_name':namelist, 'ticker_symbol':tickerlist, 'market_cap':marketcaplist, 'price':pricelist, 'percent_change_hour':changelist})

cmcdf

cmcdf.to_csv('./data/coinmarketcap.csv')