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
    h2soup = mysoup.findAll('h2')
    tdsoup = mysoup.findAll('td')
    #print webpage
    #print titlesoup
    #news.append
    
    list=[]
    list[:]=range(0,100) #27)

    #news=[]
    print "H2: ",h2soup[1]
    print "H2: ",h2soup[2]

    for i in list:
        td = tdsoup[i]
        print "TD: ",td


#read_weather()
#return news