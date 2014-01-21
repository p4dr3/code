#! /usr/bin/python

from urllib import urlopen
from bs4 import BeautifulSoup

rss_link = "http://rss.lemonde.fr/c/205/f/3050/index.rss"


webpage = urlopen(rss_link).read()
mysoup = BeautifulSoup(webpage)

titlesoup = mysoup.findAll('title')

bla = "<title> 1 <title> 23 <title>"
print bla.replace("<title>","")
print bla

for i in range(2,10):
    bla2 = string(titlesoup[i])
    print bla2.replace("<title>","")


def mafonction(a,b):
    return a+b

#blabla


print mafonction(10,20)