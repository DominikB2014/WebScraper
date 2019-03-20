from Scraper import getCar

# Set the URL you want to webscrape from
url = 'https://www.cars.com/vehicledetail/detail/746043557/overview/'
cat, value = getCar(url)
for i in range(len(cat)):
    print(cat[i],"-", value[i])
