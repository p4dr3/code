#! /usr/bin/python
from salli import play_this
from salli import say
from read_rss import read_rss
from read_weather import read_weather

user= "Anne"

#--- Greetings
voicelist=[]
voicelist.append(say("Greetings "+user+".", 'en_us_salli'))

#--- Template for Weather Forecast
#------ Today
weather = read_weather(0)
voicelist.append(say(weather,'en_us_salli'))
#------ Tomorrow
#weather = read_weather(1)
#voicelist.append(say(weather,'en_us_salli'))
#------ All week
#weather=[]
#for i in range(0,7):
#    weather.append(read_weather(i))
#weather = " ".join(weather)
#voicelist.append(say(weather,'en_us_salli'))

#--- Template for RSS
#------ FRENCH
print ("#------ FRENCH")
#--------- LA PRESSE
print ("#--------- LA PRESSE")
voicelist.append(say("Voici les nouvelles de la presse.", 'fr_mathieu'))
news=read_rss("http://rss.lapresse.ca/225.xml", 2, 4)
for item in news:
    voicelist.append(say(item,'fr_mathieu'))

#------ ENGLISH
print ("#------ ENGLISH")
#--------- LA GAZETTE
print ("#--------- LA GAZETTE")
voicelist.append(say("And now the news from the Gazette.", 'en_us_salli'))
news=read_rss("http://rss.canada.com/get/?F299", 1, 3)
for item in news:
    voicelist.append(say(item,'en_us_salli'))

#--- Sign off
voicelist.append(say("That's all for now. Have a great day.", 'en_us_salli'))

#--- Play All
play_this(voicelist)

