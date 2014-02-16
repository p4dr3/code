#! /usr/bin/python
from salli import say_that
from read_rss import read_rss
from read_weather import read_weather
# MAIN

user= "Adrian"

# works
# FRANCAIS
#rss_link = "http://rss.lemonde.fr/c/205/f/3050/index.rss"
rss_link1 = "http://rss.lapresse.ca/225.xml"
# ENGLISH
rss_link2 = "http://rss.canada.com/get/?F299"

#doesnt work (<p [..]> tags)
#rss_link = "http://feeds.gawker.com/lifehacker/full"

# Greetings
#say_that("Greetings "+user+". Hope you're doing well this morning. ", "en_us_salli") #cut before end


# Template for Weather
# Today
weather = read_weather(0)
say_that(weather,'en_us_salli')
# Tomorrow
#weather = read_weather(1)
#say_that(weather,'en_us_salli')

# Template for RSS
# FRENCH
#say_that("Les nouvelles de la presse.", "fr_mathieu")
#news=read_rss(rss_link1)
#for item in news:
#    say_that(item,"fr_mathieu")
#
# ENGLISH
#say_that("And now the news from the Gazette.", "en_us_salli")
#say_that("Never winning a major honour has not prevented Tom Finney going down as one of football's greats.","en_us_salli")
#news=read_rss(rss_link2)
#for item in news:
#    say_that(item,"en_us_salli")

# Quote of the day

# Sign off
#say_that("That's all for today. Have a great day "+user+". Talk to you soon. ", "en_us_salli")
