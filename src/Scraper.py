# Import libraries
import requests
from bs4 import BeautifulSoup
import re


def start_scrape():
    """Begins to scrape all data from cars.com"""

    response = requests.get("cars.com")

    # Parse HTML and save to Beautiful lSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    carSoup = soup.findAll("script", {"type": "text/javascript"})


def get_car(url: str):
    """Given a url to a ad, returns the properties of the vehicle"""

    categories = []
    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")
    carSoup = soup.findAll("script", {"type": "text/javascript"})

    # Scrapes the price of the vehicle
    price = soup.findAll("span", class_="vehicle-info__price-display")
    categories.append(('Price', str(price[0].text)[1:]))

    # Finds the body Style and trim of a particular vehicle
    vehicle = str(carSoup[0]).split("\n")[3]
    c = re.search('"bodyStyle":"(.*?)"', vehicle)
    t = re.search('"trim":"(.*?)"', vehicle)
    if c:
        categories.append(('Body Style', c.group(1)))
    if t:
        categories.append(('Trim', t.group(1)))

    # Extract each category and their value
    for car in soup.findAll("li", {"class": "vdp-details-basics__item"}):
        car = str(car.text).strip("\n")
        car = car.split(": ")
        categories.append((car))

    categories.append(('Link', url))
    return categories


def get_models(mk_id:str ):
    """Given a make id, returns the models of that make"""
    models = []

    # Connect to the URL
    response = requests.get(to_url(mk_id))

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")

    # Retrieves the HTML list of models
    model_soup = soup.findAll("ul", {"class": "refinements"})[3]
    model_soup = model_soup.findAll("label", class_='checkbox__label')

    # Find all the model names and their id's
    for m in model_soup:
        model = str(m.text).strip()  # Represents the model of a vehicle
        m_id = str(m).split("\"")[3].strip("mdId-")  # Represents the id of a model
        models.append((model, m_id))

    return models


def get_years(mk_id:str, md_id:str):
    """Given the make id and model id, returns the years of that car"""
    years = []

    # Connect to the URL
    response = requests.get(to_url(mk_id, md_id))

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")

    # Retrieves the HTML list of years of a particular model
    model_soup = soup.findAll("div", {"class": "select"})[2]
    year_soup = model_soup.findAll("option") # each element is a particular year

    for i in year_soup:
        years.append(i.text)

    return years

def get_year_ids():
    """Given the make id and model id, returns the years of that car"""
    year_ids = {}

    # Connect to the URL
    response = requests.get("https://www.cars.com/for-sale/searchresults.action/?rd=99999"
                            "&searchSource=ADVANCED_SEARCH&yrId=20199&yrId=20143&yrId=20198"
                            "&zc=60606")

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")

    # Retrieves the HTML list of years of a particular model
    model_soup = soup.findAll("div", {"class": "select"})[2]
    year_soup = model_soup.findAll("option")  # each element is a particular year

    for i in year_soup:
        year = i.text
        y = re.search('value="(.*?)"', str(i))
        year_ids[year] = y.group(1)

    return year_ids


def to_url(mk_id: str, md_id: str = False, yr_id: str = False ) -> str:
    """Converts to url using the id's for the: make, model, year"""

    url = "https://www.cars.com/for-sale/searchresults.action/?" \
          "rd=99999"
    end_of_url = "&zc=60606&" \
                 "stkTypId="

    if not md_id and not yr_id:
        return url + \
               "&mkId=" + mk_id + \
               "&searchSource=ADVANCED_SEARCH" + \
               end_of_url

    elif not yr_id:
        return url + \
               "&mkId=" + mk_id + \
               "&mdId=" + md_id + \
               "&searchSource=ADVANCED_SEARCH" + \
               end_of_url

    return url + \
           "&mkId=" + mk_id + \
           "&mdId=" + md_id + \
           "&searchSource=ADVANCED_SEARCH&" \
           "yrId" + yr_id + \
           end_of_url
