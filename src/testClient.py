from Scraper import *
from Constants import MAKES
import Write
import multiprocessing
from enum import Enum

# # Set the URL you want to webscrape from
url = 'https://www.cars.com/vehicledetail/detail/752964006/overview/'
url2 = 'https://www.cars.com/vehicledetail/detail/766847902/overview/'
url4 = 'https://www.cars.com/vehicledetail/detail/757712014/overview/'
# Write.init_data()
# Write.write_car("Cheverolet", "Colorado", "2019", get_car(url))
# Write.write_car("Buggatti","Veyron", "2018", get_car(url2))
# Write.write_car("Dodge", "Challenger", "2018", get_car(url4))

get_year_ids()
#
