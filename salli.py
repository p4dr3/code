#! /usr/bin/python
import base64
import requests
import StringIO
#http://base64encode.net/ and replace = by .

def encode_it(data):
    data=base64.b64encode(data)
    data=data.replace("=",".")
    return data

def get_session_id(website):
    buf = StringIO.StringIO(website)
    for line in buf:
        if line.find("voicetest.php?rtr")!= -1: 
            line = line.split("&",10)
            line = line[4].split("\"",2)
            session_id = line[0]
            #print "Session _id: "+session_id
            return session_id
    

website = "http://www.ivona.com"

text = "Hi I'm Salli and I have a sexy voice"
text= encode_it(text)

script = "/voicetest.php"
voice_id = "en_us_salli" #Salli
voice_id = encode_it(voice_id)


#header mimicing firfox
my_header = {"User-Agent":
       "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0"}

#REQUESTS 

#setup a session to keep cookies
session = requests.Session()
print "SESSION"
print session.cookies

#grabbing session id and cookie from 1st connection
response1 = session.request('GET', website)
#print response1
print "REQ1 - COOKIES"
print response1.cookies

session_id = get_session_id(response1.content) #webpage

#formating and sending http GET request
my_url = website+script
parameters = "rtr=1&t2r="+text+"&v2r="+voice_id+"&lang=en&"+session_id

myreq = requests.Request(method='GET', url = my_url, params = parameters , cookies = session.cookies )#, stream=True) #, allow_redirect =True
req = myreq.prepare()
response2 = session.send(req)

#Making sure we got what we wanted

print "REQ2 - URL"
print response2.url
print "REQ2 - HEADERS"
print response2.headers
my_mp3 = response2.content #that's my MP3
print "REQ2 - HISTORY"
print response2.history

#print my_mp3

#f = open('my_mp3.wav','w')
#f.write(response2.content) # python will convert \n to os.linesep
#f.close()





