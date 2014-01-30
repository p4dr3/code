#! /usr/bin/python
from urllib import urlopen
import urllib2
import re
import base64

#http://base64encode.net/ and replace = by .

def encode_it(data):
    data=base64.b64encode(data)
    data=data.replace("=",".")
    return data

def get_session_id(website):
    webpage = urlopen(website).readlines()
    for line in webpage:
        if line.find("voicetest.php?rtr")!= -1: 
            line = line.split("&",10)
            line = line[4].split("\"",2)
            session_id = line[0]
            print "Session _id: "+session_id
            return session_id
    

website = "http://www.ivona.com"

text = "Hi I'm Salli and I have a sexy voice"
text= encode_it(text)

script = "/voicetest.php"
voice_id = "en_us_salli" #Salli
voice_id = encode_it(voice_id)


session_id = get_session_id(website)


my_url = website+script+"?rtr=1&t2r="+text+"&v2r="+voice_id+"&lang=en&"+session_id
print my_url

#!- validated

#experimental
my_header = {"User-Agent":
       "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7"}


my_req = urllib2.Request(my_url, "", my_header)
response = urllib2.urlopen(my_url)    
page = response.read()
print "toto"
print page
#s = Sound() 
##s.read('sound.wav') 
#s.play()
          
          
         
#print webpage.split()


#print webpage(44060,40)
#for line in webpage.index:
 #   print line
