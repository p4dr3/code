#! /usr/bin/python
from salli import play_this
from salli import say
from read_rss import read_rss
from read_weather import read_weather

user= "Alex"
# RSS
# FRANCAIS
#rss_link = "http://rss.lemonde.fr/c/205/f/3050/index.rss"
rss_link1 = "http://rss.lapresse.ca/225.xml"
# ENGLISH
rss_link2 = "http://rss.canada.com/get/?F299"

#doesnt work (<p [..]> tags)
#rss_link = "http://feeds.gawker.com/lifehacker/full"

#--- Greetings
voicelist=[]
#voicelist.append(say("Greetings "+user+".", 'en_us_salli')) #cut before end

#voicelist.append(say("It's like Codecademy for learning about money. Through the site's videos, articles, and other resources, you'll learn how to read stock quotes, how to build your investment strategy, and also other personal finance basics like how to get out of debt. You can also track your portfolio on the site if you like and join \"leagues\" to compete against others with your investment picks. Since this stuff isn't taught in schools yet, it's a very welcome resource. It's like Codecademy for learning about money. Through the site's videos, articles, and other resources, you'll learn how to read stock quotes, how to build your investment strategy, and also other personal finance basics like how to get out of debt. You can also track your portfolio on the site if you like and join \"leagues\" to compete against others with your investment picks. Since this stuff isn't taught in schools yet, it's a very welcome resource." , 'en_us_salli'))

#--- Template for Weather
#------ Today
weather = read_weather(0)
voicelist.append(say(weather,'en_us_salli'))
#------ Tomorrow
#weather = read_weather(1)
#voicelist.append(say(weather,'en_us_salli'))

#--- Template for RSS
#------ FRENCH
#voicelist.append(say("Voici les nouvelles de la presse.", 'fr_celine'))
news=read_rss(rss_link1)
for item in news:
    voicelist.append(say(item,'fr_celine'))

#------ ENGLISH
#voicelist.append(say("And now the news from the Gazette.", 'en_us_salli'))
news=read_rss(rss_link2)
for item in news:
    voicelist.append(say(item,'en_us_salli'))

#--- Sign off
#voicelist.append(say("That's all for now. Have a great day.", 'en_us_salli'))

#--- Play All
play_this(voicelist)

