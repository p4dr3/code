#! /usr/bin/python
from urllib import urlopen
from bs4 import BeautifulSoup

# works
#rss_link = "http://rss.lemonde.fr/c/205/f/3050/index.rss"
rss_link = "http://rss.lapresse.ca/225.xml"

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
list[:]=range(2,10) #27)

for i in list:
    #force to unicode string ( instead of str() )
    toto = unicode(titlesoup[i]) 
    tata = unicode(descrsoup[i-1])
    
    
    #remove html tags
    toto = toto.replace("<title>", "")
    toto = toto.replace("</title>", "")
    
    tata = tata.replace("<description>", "")
    #get rid of the html after the description
    tata = tata.split ('&lt')[0]
    
    print toto
    print tata
    print ""
    
   
    
    