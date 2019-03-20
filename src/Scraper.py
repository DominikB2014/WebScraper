# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

def getCar(url:str):
    categories =[]
    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    carSoup = soup.findAll("script", {"type": "text/javascript"})

    #Scrapes the price of the vehicle
    price = str(soup.findAll("span", class_="vehicle-info__price-display"))[44:].\
        strip("</span>]").replace(',','')
    categories.append(('Price', price))

    #Finds the body Style of a particular vehicle
    body = str(carSoup[0]).split("\n")[3]
    m = re.search('"bodyStyle":"(.+?)"', body)
    if m:
        bodyStyle = m.group(1)
    categories.append(('Body Style', bodyStyle))

    #Extract each category and their value
    carSoup = soup.findAll("li", {"class": "vdp-details-basics__item"})
    for car in carSoup:
        car = str(car)[46:-13].split(":</strong><span> ")
        categories.append((car[0], car[1]))

    return

def start_scrape():
    response = requests.get(cars.com)

    # Parse HTML and save to Beautiful lSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    carSoup = soup.findAll("script", {"type": "text/javascript"})
