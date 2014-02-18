#! /usr/bin/python
from salli import say_that
from read_rss import read_rss
from read_weather import read_weather

user= "Alex"
# RSS
# works
# FRANCAIS
#rss_link = "http://rss.lemonde.fr/c/205/f/3050/index.rss"
rss_link1 = "http://rss.lapresse.ca/225.xml"
# ENGLISH
rss_link2 = "http://rss.canada.com/get/?F299"
#doesnt work (<p [..]> tags)
#rss_link = "http://feeds.gawker.com/lifehacker/full"

# Greetings
say_that("Greetings "+user+". ", 'en_us_salli',1) #cut before end

# Template for Weather
#
#     Today
#
weather = read_weather(0)
say_that(weather,'en_us_salli',0)
#
#     Tomorrow
#
#weather = read_weather(1)
#say_that(weather,'en_us_salli')

# Template for RSS
#
#     FRENCH
#
#say_that("Voici les nouvelles de la presse.", 'fr_mathieu')
#news=read_rss(rss_link1)
#for item in news:
#    say_that(item,'fr_mathieu')
#
#     ENGLISH
#
say_that("And now the news from the Gazette.", 'en_us_salli',0)
news=read_rss(rss_link2)
for item in news:
    say_that(item,'en_us_salli',0)

# Sign off
#say_that("That's all for now. Have a great day.", 'en_us_salli')

