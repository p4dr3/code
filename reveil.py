#! /usr/bin/python

from urllib import urlopen
from bs4 import BeautifulSoup

rss_link = "http://rss.lemonde.fr/c/205/f/3050/index.rss"


webpage = urlopen(rss_link).read()
mysoup = BeautifulSoup(webpage)

titlesoup = mysoup.findAll('title')
print titlesoup

list=[]
list[:]=range(2,10)

for i in list:
    print titlesoup[i]