#! /usr/bin/python
import re
from urllib import urlopen
from bs4 import BeautifulSoup

def _callback(matches):
    id = matches.group(1)
    try:
        return unichr(int(id))
    except:
        return id

def decode_unicode_references(data):
    #return re.sub("&#(\d+)(;|(?=\s))", _callback, data)
    return re.sub("&amp;#(\d+)(;|(?=\s))", _callback, data)

# Reads a rss link, parses it and returns an array of news title/articles
def read_rss(rss_link):
    #read webpage and stores it
    webpage = urlopen(rss_link).read()

    #import to beautifulsoup
    mysoup = BeautifulSoup(webpage)

    #parsing
    titlesoup = mysoup.findAll('title')
    descrsoup = mysoup.findAll('description')

    list=[]
    list[:]=range(2,4) #27)

    news=[]
    for i in list:

        title = titlesoup[i]
        descr = descrsoup[i]

        #convert to unicode
        title = unicode(title)
        descr = unicode(descr)

        #remove html tags
        title = title.replace("<title>", "")
        title = title.replace("</title>", "")
        descr = descr.replace("<description>", "")
        descr = descr.replace("</description>", "")

        #get rid of the html after the description
        descr = descr.split ('&lt')[0]

        title= str(title+".\n")
        descr = str(descr)

        title = decode_unicode_references(title)
        descr = decode_unicode_references(descr)

        news.append (title)
        news.append (descr)
      
    return news

#debug stuff:
    #print type(descr)
