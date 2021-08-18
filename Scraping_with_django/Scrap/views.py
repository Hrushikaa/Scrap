from django.shortcuts import render
from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', {'link':'http://127.0.0.1:8000/'})

def twitter(request):
    return render(request, 'twitter.html')

def youtube(request):
    return render(request, 'youtube.html')

def crypto(request):
    return render(request, 'crypto.html')


def about(request):
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')


def scrap_twitter():
    trend_name = []
    count = []

    page = requests.get('https://twitter-trends.iamrohit.in/india')
    soup = bs4(page.text, 'html.parser')
    for i in soup.find_all('a', class_="tweet"):
        ttl = i.getText()
        trend_name.append(ttl)

    for j in soup.find_all('span', class_="badge"):
        cnt = j.getText()
        count.append(cnt)

    data = { 'Twitter Trending Hashtags': trend_name, 'Tweet Volume': count}
    df = pd.DataFrame(data=data)
    # df.index += 1
    df.index.name = 'No.'
    df.index+=1
    df.to_csv('utils1/df_output.csv', encoding='latin1')

    file = pd.read_csv("utils1/df_output.csv")
    file.to_html("templates/index10.html", index=False)

def yt():
    trend_name = []
    count = []

    page = requests.get('https://yt-trends.iamrohit.in/India')
    soup = bs4(page.text, 'html.parser')
    # for i in soup.find_all('tbody', id="copyData"):
    for i in soup.find_all('a', class_="pl"):
        ttl = i.getText()
        # ttl = ttl.replace('Tweets', '')
        trend_name.append(ttl)

    while (" " in trend_name):
        trend_name.remove(" ")
    while ("[ReadMore..]" in trend_name):
        trend_name.remove("[ReadMore..]")
    # print(trend_name)
    #
    for j in soup.find_all('p', style='color:green;'):
        cnt = j.getText()

        count.append(cnt)
    # print(count)

    data = {'Youtube trending': trend_name, 'Details': count}
    df = pd.DataFrame(data=data)
    df.index += 1
    df.index.name = 'No.'
    df.to_csv('utils1/ytoutput.csv', encoding='latin1')

    file = pd.read_csv("utils1/ytoutput.csv")
    file.to_html("templates/ytindex.html", index=False)

def crypt():
    trend_name = []
    count = []
    marketcap = []
    Volume = []
    CirculatingSupply = []

    page = requests.get('https://coinmarketcap.com/')
    soup = bs4(page.text, 'html.parser')

    for i in soup.find_all('p', class_="sc-1eb5slv-0 iJjGCS"):
        ttl = i.getText()
        trend_name.append(ttl)

    for j in soup.find_all('div', class_="sc-131di3y-0 cLgOOr"):
        cnt = j.getText()
        count.append(cnt)

    for j in soup.find_all('span', class_="sc-1ow4cwt-0 iosgXe"):
        mtc = j.getText()
        marketcap.append(mtc)

    for j in soup.find_all('p', class_="sc-1eb5slv-0 kDEzev font_weight_500___2Lmmi"):
        vl = j.getText()
        Volume.append(vl)

    for j in soup.find_all('p', class_="sc-1eb5slv-0 hNpJqV"):
        cs = j.getText()
        CirculatingSupply.append(cs)

    data = {'Name': trend_name, 'Price': count, 'Market Cap': marketcap, 'Volume(24h)': Volume,
            'Circulating Supply': CirculatingSupply}
    df = pd.DataFrame(data=data)

    df.to_csv('utils1/cryptoutput.csv', encoding='latin1', index=False)

    file = pd.read_csv("utils1/cryptoutput.csv")
    file.to_html("templates/cryptindex.html", index=False)



filenames = ['/Users/hrushika/PycharmProjects/Scrap/Scraping_with_django/templates/base.html', '/Users/hrushika/PycharmProjects/Scrap/Scraping_with_django/templates/index10.html']
filenames2 = ['/Users/hrushika/PycharmProjects/Scrap/Scraping_with_django/templates/base.html', '/Users/hrushika/PycharmProjects/Scrap/Scraping_with_django/templates/ytindex.html']
filenames3 = ['/Users/hrushika/PycharmProjects/Scrap/Scraping_with_django/templates/base.html', '/Users/hrushika/PycharmProjects/Scrap/Scraping_with_django/templates/cryptindex.html']


with open('/Users/hrushika/PycharmProjects/Scrap/Scraping_with_django/templates/twitter.html', 'w') as outfile:

    for names in filenames:
        # Open each file in read mode
        with open(names) as infile:
            outfile.write(infile.read())

        outfile.write("\n")

with open('/Users/hrushika/PycharmProjects/Scrap/Scraping_with_django/templates/youtube.html', 'w') as outfile:

    for names in filenames2:
        # Open each file in read mode
        with open(names) as infile:
            outfile.write(infile.read())

        outfile.write("\n")

with open('/Users/hrushika/PycharmProjects/Scrap/Scraping_with_django/templates/crypto.html', 'w') as outfile:

    for names in filenames3:
        # Open each file in read mode
        with open(names) as infile:
            outfile.write(infile.read())

        outfile.write("\n")

scrap_twitter()
yt()
crypt()
