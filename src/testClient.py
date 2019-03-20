from Scraper import *
import Write

# Set the URL you want to webscrape from
url = 'https://www.cars.com/vehicledetail/detail/752964006/overview/'
url2 = 'https://www.cars.com/vehicledetail/detail/766847902/overview/'
url3 = 'https://www.cars.com/vehicledetail/detail/759929739/overview/'
url4 = 'https://www.cars.com/vehicledetail/detail/757712014/overview/'
Write.init_data()
Write.write_car("Cheverolet", "Colorado", "2019", getCar(url))
Write.write_car("Buggatti","Veyron", "2018", getCar(url2))
Write.write_car("Audi", "RS5", "2019", getCar(url3))
Write.write_car("Dodge", "Challenger", "2018", getCar(url4))

