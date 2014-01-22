#! /usr/bin/python
from urllib import urlopen
from bs4 import BeautifulSoup

# voice requires pyttsx which requires [setuptools] to install
import pyttsx
# voice on windows requires [pywin32] to access OS default TextToSpeech

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

#debug
#print titlesoup

list=[]
list[:]=range(1,5) #27)

#setup voice

engine = pyttsx.init()
#check current voice setup
voices = engine.getProperty('voices')
for voice in voices:
    print voice 
    


for i in list:
    #force to unicode string ( instead of str() )
    title = unicode(titlesoup[i]) 
    descr = unicode(descrsoup[i])
     
    #remove html tags
    title = title.replace("<title>", "")
    title = title.replace("</title>", "")
    
    descr = descr.replace("<description>", "")
    descr = descr.replace("</description>", "")
    #get rid of the html after the description
    descr = descr.split ('&lt')[0]
    
    print title
    engine.say(title)
    print descr
    engine.say(descr)
    print ""

engine.runAndWait()

#bla
    