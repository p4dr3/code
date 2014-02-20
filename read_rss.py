#! /usr/bin/python
import re
from urllib import urlopen
from bs4 import BeautifulSoup

def _callback(matches):
    my_id = matches.group(1)
    try:
        return unichr(int(my_id))
    except:
        return my_id

def decode_unicode_references(data):
    return re.sub("&#(\d+)(;|(?=\s))", _callback, data)
    #return re.sub("&amp;#(\d+)(;|(?=\s))", _callback, data)


#--------------------------------------------------------------------------#
# Reads a rss link, parses it and returns an array of news title/articles
#--------------------------------------------------------------------------#
def read_rss(rss_link):
    #read webpage and stores it
    webpage = urlopen(rss_link).read()

    #import to beautifulsoup
    mysoup = BeautifulSoup(webpage)

    #parsing
    titlesoup = mysoup.findAll('title')
    descrsoup = mysoup.findAll('description')

    my_list=[]
    my_list[:]=range(2,4) #27)

    news=[]
    for i in my_list:

        title = titlesoup[i]
        title = title.findAll(text=True)[0]
        descr = descrsoup[i]
        descr = descr.findAll(text=True)[0]

        # Convert to unicode
        title = unicode(title)
        descr = unicode(descr)

        # Get rid of the html after the description
        descr = descr.split ('<')[0]

        title= str(title+".\n")
        descr = str(descr+".\n")

        # making sure we have a single . at the end of the string
        r = re.compile(r"(\.+)")
        #print "title/",title
        r.sub('.', title)
        #print "title/",title

        #print "descr/",descr
        r.sub('.', descr)
        #print "descr/",descr

        #descr = "".join(descr.split('.'))



        title = decode_unicode_references(title)
        descr = decode_unicode_references(descr)

        news.append (title)
        news.append (descr)

    return news

#debug stuff:
    #print type(descr)
