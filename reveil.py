#! /usr/bin/python
from salli import say_that
from read_rss import read_rss
from read_weather import read_weather
# MAIN

# works
# FRANCAIS
#rss_link = "http://rss.lemonde.fr/c/205/f/3050/index.rss"
rss_link1 = "http://rss.lapresse.ca/225.xml"
# ENGLISH
rss_link2 = "http://rss.canada.com/get/?F299"

#doesnt work (<p [..]> tags)
#rss_link = "http://feeds.gawker.com/lifehacker/full"


#read_weather()

say_that("Les nouvelles de la presse.", "fr_celine")
news=read_rss(rss_link1)
for item in news:
    say_that(item,"fr_celine")

say_that("And now the news from the Gazette.", "en_us_salli")
news=read_rss(rss_link2)
for item in news:
    say_that(item,"en_us_salli")