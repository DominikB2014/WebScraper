# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def getCar(url:str):
    categories = ['price']
    values = []
    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    carSoup = soup.findAll('li', class_="vdp-details-basics__item")

    #Scrapes the price of the vehicle
    price = str(soup.findAll("span", class_="vehicle-info__price-display"))[44:].strip("</span>]")
    values.append(price)

    #Extract each category and their value
    for car in carSoup:
        car = str(car)[46:-13].split(":</strong><span> ")
        categories.append(car[0])
        values.append(car[1])

    return categories, values

# Set the URL you want to webscrape from
url = 'https://www.cars.com/vehicledetail/detail/746043557/overview/'
cat, val = getCar(url)
print(cat)
print(val)