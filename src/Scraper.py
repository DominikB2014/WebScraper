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
    price = soup.findAll("span", class_="vehicle-info__price-display")
    categories.append(('Price', str(price[0].text)[1:-1]))

    #Finds the body Style of a particular vehicle
    body = str(carSoup[0]).split("\n")[3]
    c = re.search('"bodyStyle":"(.+?)"', body)
    if c:
        body = c.group(1)
    categories.append(('Body Style', body))

    #Extract each category and their value
    for car in soup.findAll("li", {"class": "vdp-details-basics__item"}):
        car = str(car.text).strip("\n")
        car = car.split(": ")
        categories.append((car[0], car[1]))

    return categories

def start_scrape():
    response = requests.get(cars.com)

    # Parse HTML and save to Beautiful lSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    carSoup = soup.findAll("script", {"type": "text/javascript"})
