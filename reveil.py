#! /usr/bin/python
from urllib import urlopen
from bs4 import BeautifulSoup

rss_link = "http://rss.lemonde.fr/c/205/f/3050/index.rss"

#read webpage and stores it
webpage = urlopen(rss_link).read()

#import to beautifulsoup
mysoup = BeautifulSoup(webpage)

#parsing
titlesoup = mysoup.findAll('title')

#debug
#print titlesoup

list=[]
list[:]=range(2,10)

for i in list:
    toto = str(titlesoup[i]) #force to string
    #remove html tags
    toto = toto.replace("<title>", "")
    toto = toto.replace("</title>", "")
    print toto
    