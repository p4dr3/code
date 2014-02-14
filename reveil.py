#! /usr/bin/python
from salli import text_to_voice

from urllib import urlopen
from bs4 import BeautifulSoup
import re
import os

def _callback(matches):
    id = matches.group(1)
    try:
        return unichr(int(id))
    except:
        return id

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ADD SUPPORT FOR NON-ASCII characters

def decode_unicode_references(data):
    #return re.sub("&#(\d+)(;|(?=\s))", _callback, data)
    return re.sub("&amp;#(\d+)(;|(?=\s))", _callback, data)


def say_that(text):
    #en_us_salli | fr_mathieu | fr_celine| fr_ca_chantal
    #ru_tatyana
    voice = text_to_voice(text, "fr_celine");

    # save voice to a file
    f = open('sound', 'wb') # important to use b we want to write as binary
    #print f
    f.write(voice)

    # plays the file with media player classic
    #os.system ("\"C:\Program Files (x86)\MPC-HC\mpc-hc.exe\" sound")
    test =" \"C:\mplayerc.exe\" sound"

    print test
    os.system (test)

# works
# FRANCAIS
#rss_link = "http://rss.lemonde.fr/c/205/f/3050/index.rss"
#rss_link = "http://rss.lapresse.ca/225.xml"
# ENGLISH
rss_link = "http://rss.canada.com/get/?F299"

#doesnt work (<p [..]> tags)
#rss_link = "http://feeds.gawker.com/lifehacker/full"


#read webpage and stores it
webpage = urlopen(rss_link).read()

#import to beautifulsoup
mysoup = BeautifulSoup(webpage)

#parsing
titlesoup = mysoup.findAll('title')
descrsoup = mysoup.findAll('description')

list=[]
list[:]=range(2,4) #27)

news = ""
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


    title= str(title)
    descr = str(descr)
    descr = descr.replace("","")
    title = decode_unicode_references(title)
    descr = decode_unicode_references(descr)

    news = news+title+".\n"
    print title+"."
    print descr
    #say_that(title)
    #print ""

print "NEWS: "+news
say_that(news)


#debug stuff:
    #print type(descr)