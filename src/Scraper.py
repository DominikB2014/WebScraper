# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://www.cars.com/vehicledetail/detail/763617323/overview/'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")
catSoup = soup.findAll('strong')
carSoup = soup.findAll('span')

car = str(carSoup).split('</span>')
for i in car:
    print(i)

category = str(catSoup).split('</strong>')[0:8]
category[0] = category[0][9:19]
for i in range(1,len(category)):
    category[i] = category[i][10:]

print(category)
