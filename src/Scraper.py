# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

def getCar(url:str):
    categories = ['Price']
    values = []
    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    carSoup = soup.findAll("script", {"type": "text/javascript"})
    car = str(carSoup[0]).split("\n")[3]
    print(car)
    car = car.split(',')[]
    for i in car:
        print(i)

    # #Scrapes the price of the vehicle
    # price = str(soup.findAll("span", class_="vehicle-info__price-display"))[44:].strip("</span>]")
    # values.append(price)
    #
    # #Extract each category and their value
    # for car in carSoup:
    #     car = str(car)[46:-13].split(":</strong><span> ")
    #     categories.append(car[0])
    #     values.append(car[1])

    return categories, values