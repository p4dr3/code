#! /usr/bin/python
import base64
import requests
import StringIO
import subprocess

# http://base64encode.net/
def encode_it(data):
    data=base64.b64encode(data)
    return data

#-------------------------------------------------------#
# Split a string into an array of short sentences each shorter than value
#-------------------------------------------------------#
def modulo_text(text, mod_value, separator):
    result=[]
    word_lst = text.split(separator)
    num_word=len(word_lst)
    i=0
    while i != num_word:
        part_text = word_lst[i]
        while ((i<=num_word-1) and (len(part_text+separator+word_lst[i])<mod_value)):
            part_text =part_text+separator+word_lst[i]
            i=i+1
        result.append(part_text)
    return result

#-------------------------------------------------------#
# Parses a webpage to extract the session_id
#-------------------------------------------------------#
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

#-------------------------------------------------------#
# Converts a string to a binary stream of mpeg voice
#-------------------------------------------------------#
def text_to_voice(text, voice):

    # Prep the text
    print text
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
    return my_voice


def say(text,voice):
    # Separator for words is " " but "." gives more fluent sentences.
    # The downside is you can't have a sentence longer than mod_value(ie 250char)
    lst_txt = modulo_text(text,250,".")
    lst_voice =[]

    for t_item in lst_txt:
        v_item = text_to_voice(t_item,voice)
        lst_voice.append(v_item)

    voice= ''.join(lst_voice)
    return voice

#-------------------------------------------------------#
# create an MPEG file from the binary list and plays it
#-------------------------------------------------------#
def play_this(voicelist):

    # Write to file
    f = open('sound', 'wb') # important to use b we want to write as binary
    for item in voicelist:
        f.write(item)
    f.close

    # Spawn MediaPlayer
    subprocess.Popen("C:\mplayerc.exe /play /close sound", shell=False, stdin=None, stdout=None, stderr=None, close_fds=False)
