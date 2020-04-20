from django.shortcuts import render
import requests
import re
from bs4 import BeautifulSoup

#WIRED
wired_r = requests.get("https://www.wired.com/category/science/")
wired_soup = BeautifulSoup(wired_r.content, 'html5lib')
wired_headings = wired_soup.find_all('h2')
wired_headings = wired_headings[0:-6] # removing footers
wired_news = []
wired_links = []
for n in wired_headings:
    wired_news.append(n.text)


#Science News
sci_r = requests.get("https://www.sciencenews.org/")
sci_soup = BeautifulSoup(sci_r.content, 'html5lib')
sci_headings = sci_soup.findAll('h2')
sci_headings = sci_headings[0:-8]
sci_news = []
for n in sci_headings:
    sci_news.append(n.text)

#NYT News
nyt_r = requests.get("https://www.nytimes.com/section/science")
nyt_soup = BeautifulSoup(nyt_r.content, 'html5lib')
nyt_headings = nyt_soup.findAll('h2')
nyt_headings = nyt_headings[1:-22]
nyt_news = []
for n in nyt_headings:
    nyt_news.append(n.text)

#Science Magazine
scimag_r = requests.get("https://www.sciencemag.org/news")
scimag_soup = BeautifulSoup(scimag_r.content, 'html5lib')
scimag_headings = scimag_soup.findAll('h2')
scimag_headings = scimag_headings[7:-42]
scimag_news = []
for n in scimag_headings:
    scimag_news.append(n.text)


#tech crunch
us_r = requests.get("https://techcrunch.com/")
us_soup = BeautifulSoup(us_r.content, 'html5lib')
us_headings = us_soup.findAll('h2')
us_headings = us_headings[1:-13]
us_news = []
for n in us_headings:
    us_news.append(n.text)

#Mind Hacks
mh_r = requests.get("https://mindhacks.com/")
mh_soup = BeautifulSoup(mh_r.content, 'html5lib')
mh_headings = mh_soup.findAll('h2')
mh_headings = mh_headings[0:7]
mh_news = []
for n in mh_headings:
    mh_news.append(n.text)

#Vox Science
dm_r = requests.get("https://www.vox.com/science-and-health")
dm_soup = BeautifulSoup(dm_r.content, 'html5lib')
dm_headings = dm_soup.findAll('h2')
dm_headings = dm_headings[4:11]
dm_news = []
for n in dm_headings:
    dm_news.append(n.text)


#Reuters
reuters_r = requests.get("https://www.npr.org/sections/science/")
reuters_soup = BeautifulSoup(reuters_r.content, 'html5lib')
reuters_headings = reuters_soup.findAll('h2')
#reuters_headings = reuters_headings[7:-42]
reuters_news = []
reuters_headings = reuters_headings[0:-18]
for n in reuters_headings:
    reuters_news.append(n.text)
print(reuters_news)


#SEND TO HTML
def index(req):
    return render(req, 'news/index.html', {'reuters_news':reuters_news, 'dm_news':dm_news,	'mh_news':mh_news, 'us_news':us_news,'wired_news':wired_news, 'wired_links':wired_links, 'sci_news': sci_news, 'nyt_news':nyt_news, 'scimag_news':scimag_news})
