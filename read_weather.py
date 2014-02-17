#! /usr/bin/python
import re
from urllib import urlopen
from bs4 import BeautifulSoup

def full_month(date):
    date = date.replace('Jan','January')
    date = date.replace('Feb','February')
    date = date.replace('Mar','March')
    date = date.replace('Apr','April')
    date = date.replace('Jun','June')
    date = date.replace('Jul','July')
    date = date.replace('Aug','August')
    date = date.replace('Sep','September')
    date = date.replace('Oct','October')
    date = date.replace('Nov','November')
    date = date.replace('Dec','December')
    return(date)

def read_weather(day):

    webpage = urlopen("http://weatherspark.com/forecasts/yr/Canada/QC/Montreal").read()
    # import to beautifulsoup
    pagesoup = BeautifulSoup(webpage)

    # parsing date
    forecast_item = pagesoup.findAll(attrs={'class' : 'forecast-feed-item'})
    forecast_item_soup = BeautifulSoup(str(forecast_item[day]))
    h2 = forecast_item_soup.findAll('h2')
    h2soup = BeautifulSoup(str(h2))
    date = h2soup.findAll(text=True)
    date = ''.join(date)
    date = date.replace('[','')
    date = date.replace(']','')
    date = full_month(date)

    # parsing forecast
    td_text = forecast_item_soup.findAll(attrs={'class' : 'text'})
    td_text_soup = BeautifulSoup(str(td_text))
    forecast = td_text_soup.findAll(text=True)
    forecast = ''.join(forecast)
    forecast = forecast.replace('[','')
    forecast = forecast.replace(']','')
    forecast = " ".join(forecast.split()) #remove extra whitespace

    # parsing temperatures
    unit_temp = forecast_item_soup.findAll('span', attrs={'class' : 'unit temperature'})
    # temp max
    temp_max = unit_temp[0]
    temp_max = re.search(r"(.\d+\.\d+)", str(temp_max))
    temp_max = int(round(float(temp_max.group(1))))
    weather="Weather forecast for "+date+". Weather is going to be "+forecast+". Temperature is going to be around "+str(temp_max)+"."
    
    # temp min
    temp_min="stupid_placeholder"
    if (len(unit_temp))==2:
        temp_min = unit_temp[1]
        temp_min = re.search(r"(.\d+\.\d+)", str(temp_min))
        temp_min = int(round(float(temp_min.group(1))))
        weather="Weather forecast for "+date+". Weather is going to be "+forecast+". Temperatures are going to be between "+str(temp_min)+" and "+str(temp_max)+"."

    return weather

