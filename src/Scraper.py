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


def get_models(mk_id):
    """Given a make name, returns the models of that make"""
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
        m_id = str(m).split("\"")[3].strip("mdId-") # Represents the id of a model
        models.append((model, m_id))

    return models




    # models = str(model_soup.text).replace("  ", "")
    # models = models.replace("\n"," ").strip().split("      ")
    # print(models)






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
