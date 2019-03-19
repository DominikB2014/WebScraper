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
    price = str(soup.findAll("span",  ))[44:].strip("</span>]")
    values.append(price)
    for car in carSoup:
        print(str(car)[30:])

#Comment

    print(carSoup)


# Set the URL you want to webscrape from
url = 'https://www.cars.com/vehicledetail/detail/746043557/overview/'
getCar(url)

# for i in range(len(titles) - 1):
#     car.append(str(carSoup[i]).split("<span> ")[-1].strip("</span>\n</li>"))e

# catSoup = soup.findAll('strong')
# carSoup = soup.findAll('span')


# car = str(carSoup).split('</span>, ')[30:38]
# category = str(catSoup).split('</strong>')[0:8]
# category[0] = category[0][9:19]
# car[0] = car[0][7:]
#
# # for i in range(1,len(category)):
# #     category[i] = category[i][10:]
# #     car[i] = car[i][7:]
# #     print(category[i], car[i])
