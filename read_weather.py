#! /usr/bin/python
import re
from urllib import urlopen
from bs4 import BeautifulSoup

def read_weather():
    #read webpage and stores it
    webpage = urlopen("http://weatherspark.com/forecasts/yr/Canada/QC/Montreal").read()

    #import to beautifulsoup
    mysoup = BeautifulSoup(webpage)

    #news=[]

    #parsing
    titlesoup = mysoup.findAll('div class=\"forecast\"')
    print "ypoyp"
    print titlesoup
    #news.append
    
#return news