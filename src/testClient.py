from Scraper import *
import Write

# Set the URL you want to webscrape from
url = 'https://www.cars.com/vehicledetail/detail/752964006/overview/'
url2 = 'https://www.cars.com/vehicledetail/detail/766847902/overview/'
Write.init_data()
Write.write_car(getCar(url))
Write.write_car(getCar(url2))

