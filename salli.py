#! /usr/bin/python
import base64
import requests
import StringIO
from time import sleep
from subprocess import Popen

# http://base64encode.net/
def encode_it(data):
    data=base64.b64encode(data)
    return data

# Parses a webpage to extract the session_id
def get_session_id(website):
    buf = StringIO.StringIO(website)
    for line in buf:
        if line.find('voicetest.php?rtr')!= -1:
            line = line.split("&",10)
            line = line[4].split("\"",2)
            session_id = line[0]
            session_id = session_id.split('=')
            #print "Session _id: "+session_id
            return session_id

# Converts a string to a binary stream of mpeg voice
def text_to_voice(text, voice):

    # Prep the text
    text=text.encode('utf-8')
    text= encode_it(text)

    # Prep the voice id  --- CAN ADD MORE
    voice_id = encode_it(voice)

    # Site specific stuff
    website = "http://www.ivona.com"
    script = "voicetest.php"

    # HTTP REQUESTS
    #header mimicing firfox
    #my_header = {"User-Agent":
    #   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0"}
    # Setup a session to keep cookies
    session = requests.Session()
    #print "SESSION"
    #print session.cookies

    # Grabbing session id and cookie from 1st request
    response1 = session.request('GET', website)
    #print response1
    #print "REQ1 - COOKIES"
    #print response1.cookies
    session_id = get_session_id(response1.content) #webpage

    # Formating and sending http GET request - 2nd request
    my_url = website+"/"+script
    parameters = {'rtr': '1', 't2r': text, 'v2r':voice_id, 'lang': 'us', session_id[0]: session_id[1]}
    myreq = requests.Request(method='GET', url = my_url, params = parameters , cookies = session.cookies )#, stream=True) #, allow_redirect =True
    req = myreq.prepare()
    response2 = session.send(req)

    # Making sure we got what we wanted
    #print "REQ2 - URL"
    #print response2.url
    #print "REQ2 - HEADERS"
    #print response2.headers
    my_voice = response2.content #that's my translated text in MPEG
    #print "REQ2 - HISTORY"
    #print response2.history

    # Write to file
    f = open('sound', 'wb') # important to use b we want to write as binary
    f.write(my_voice)
    f.close

# Converts a text to played sound
def say_that(text,speaker):

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # DEAL WITH TEXT LENGHT HERE
    #if len(text) > 250
    #    lst = str.split(text,'.')
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    text_to_voice(text, speaker);
    print text

    # plays the file with media player classic
    Popen("C:\mplayerc.exe sound", shell=False, stdin=None, stdout=None, stderr=None, close_fds=True)

    # wait a bit to let audio play entirely, speed depends on speaker
    words= len(text.split())
    print "WORDS/2 ",words/2
    print "TXT LEN/NUM",(len(text))/20

    if speaker == 'en_us_salli':
        wait_time = ((words/2 +((len(text))/20))/2)+0.5
    if speaker == 'fr_celine':
        wait_time = (((words-2)/2 +((len(text))/20))/2)
    if speaker == 'fr_mathieu':
        wait_time = ((words/2 +((len(text))/20))/2)-0.5

    # for really short sentences
    if wait_time <2:
        wait_time=2

    print "WAIT: "+str(wait_time)
    print ""
    sleep(wait_time)

