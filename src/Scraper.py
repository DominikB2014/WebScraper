# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re


def get_car(url: str):
    categories = []
    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    carSoup = soup.findAll("script", {"type": "text/javascript"})

    # Scrapes the price of the vehicle
    price = soup.findAll("span", class_="vehicle-info__price-display")
    categories.append(('Price', str(price[0].text)[1:-1]))

    # Finds the body Style of a particular vehicle
    body = str(carSoup[0]).split("\n")[3]
    c = re.search('"bodyStyle":"(.+?)"', body)
    if c:
        body = c.group(1)
    categories.append(('Body Style', body))

    # Extract each category and their value
    for car in soup.findAll("li", {"class": "vdp-details-basics__item"}):
        car = str(car.text).strip("\n")
        car = car.split(": ")
        categories.append((car[0], car[1]))

    return categories


def to_url(mk_id: str, md_id: str = False, yr_id: str = False) -> str:
    """Converts to url using the id's for the: make, model, year"""

    url = "https://www.cars.com/for-sale/searchresults.action/?" \
          "rd=99999"
    end_of_url = "&zc=60606&" \
                 "stkTypId=28880"

    if not md_id and not yr_id:
        return url + \
               "&mkId=" + mk_id + \
               "&searchSource=ADVANCED_SEARCH" + \
               end_of_url

    elif not yr_id:
        return url + \
               "&mkId" + mk_id + \
               "&mdId=47843" \
               "&searchSource=ADVANCED_SEARCH" + \
               end_of_url

    return url + \
           "&mkId=" + mk_id + \
           "&mdId=" + md_id + \
           "&searchSource=ADVANCED_SEARCH&" \
           "yrId" + yr_id + \
           end_of_url


def start_scrape():
    """Begins to scrape all data from cars.com"""

    response = requests.get(cars.com)

    # Parse HTML and save to Beautiful lSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    carSoup = soup.findAll("script", {"type": "text/javascript"})
