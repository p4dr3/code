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
    #return re.sub("&#(\d+)(;|(?=\s))", _callback, data)
    return re.sub("&amp;#(\d+)(;|(?=\s))", _callback, data)
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
list[:]=range(1,5) #27)

#setup voice
engine = pyttsx.init()
#check current voice setup
voices = engine.getProperty('voices')
for voice in voices:
    print voice
    
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
    title = decode_unicode_references(title)
    descr = decode_unicode_references(descr)

    print title+"."
    #engine.say(title)
    print descr
    #engine.say(descr)
    print ""
    
engine.runAndWait()
    

#debug stuff:
    #print type(descr)