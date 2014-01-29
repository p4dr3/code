#! /usr/bin/python
from urllib import urlopen
from bs4 import BeautifulSoup

# voice requires pyttsx which requires [setuptools] to install
import pyttsx
# voice on windows requires [pywin32] to access OS default TextToSpeech

import re
def _callback(matches):
    id = matches.group(1)
    try:
        return unichr(int(id))
    except:
        return id

def decode_unicode_references(data):
    return re.sub("&#(\d+)(;|(?=\s))", _callback, data)

# works
#rss_link = "http://rss.lemonde.fr/c/205/f/3050/index.rss"
#rss_link = "http://rss.lapresse.ca/225.xml"

rss_link = "http://rss.canada.com/get/?F299"
#doesnt work
#rss_link = "http://feeds.gawker.com/lifehacker/full"


#read webpage and stores it
webpage = urlopen(rss_link).read()

#import to beautifulsoup
mysoup = BeautifulSoup(webpage)

#parsing
titlesoup = mysoup.findAll('title')
descrsoup = mysoup.findAll('description')

list=[]
list[:]=range(1,5) #27)

#setup voice

engine = pyttsx.init()
#check current voice setup
voices = engine.getProperty('voices')
for voice in voices:
    print voice 
    
for i in list:
    
    #remove html tags
    title = titlesoup[i].get_text() 
    descr = descrsoup[i].get_text()
    #convert to unicode
    title = unicode (title)
    title = decode_unicode_references(title)
    descr = unicode (descr)
    descr = decode_unicode_references(descr)
    
    print title
    engine.say(title)
    print descr
    engine.say(descr)
    print ""

engine.runAndWait()


#bla
    